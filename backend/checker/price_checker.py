"""Проверка цен и отправка уведомлений"""
import threading
import time
from typing import Callable, List
from datetime import datetime
from backend.api import CoingeckoAPI
from backend.models import Alert


class PriceChecker:
    """Фоновый процесс для проверки цен"""

    def __init__(self, on_alert: Callable):
        """
        Инициализировать проверку цен

        Args:
            on_alert: Callback функция при срабатывании оповещения
        """
        self.api = CoingeckoAPI()
        self.on_alert = on_alert
        self.is_running = False
        self.thread = None
        self.check_interval = 5  # в минутах
        self.last_prices = {}

    def start(self, alerts: List[Alert], check_interval: int = 5) -> None:
        """
        Запустить проверку цен

        Args:
            alerts: Список оповещений
            check_interval: Интервал проверки в минутах
        """
        if self.is_running:
            return

        self.is_running = True
        self.check_interval = check_interval
        self.alerts = alerts

        self.thread = threading.Thread(target=self._check_loop, daemon=True)
        self.thread.start()
        print(f"[{self._timestamp()}] Проверка цен запущена (интервал: {check_interval} мин)")

    def stop(self) -> None:
        """Остановить проверку цен"""
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=2)
        print(f"[{self._timestamp()}] Проверка цен остановлена")

    def update_alerts(self, alerts: List[Alert]) -> None:
        """Обновить список оповещений"""
        self.alerts = alerts

    def _check_loop(self) -> None:
        """Основной цикл проверки"""
        while self.is_running:
            try:
                self._check_prices()
            except Exception as e:
                print(f"[{self._timestamp()}] Ошибка при проверке: {e}")

            # Ждем перед следующей проверкой
            sleep_time = self.check_interval * 60
            for _ in range(sleep_time):
                if not self.is_running:
                    break
                time.sleep(1)

    def _check_prices(self) -> None:
        """Проверить цены всех монет"""
        if not self.alerts:
            return

        # Получить уникальные монеты
        coins = list(set(a.coin.lower() for a in self.alerts))

        # Получить цены
        prices = self.api.get_prices_multiple(coins)

        if not prices:
            print(f"[{self._timestamp()}] Не удалось получить цены")
            return

        # Проверить каждое оповещение
        for alert in self.alerts:
            if not alert.active:
                continue

            coin_id = alert.coin.lower()
            if coin_id not in prices:
                continue

            current_price = prices[coin_id]

            # Проверить условие
            triggered = False
            if alert.condition == "above" and current_price >= alert.price:
                triggered = True
            elif alert.condition == "below" and current_price <= alert.price:
                triggered = True

            if triggered:
                self._trigger_alert(alert, current_price)

    def _trigger_alert(self, alert: Alert, current_price: float) -> None:
        """Вызвать callback при срабатывании оповещения"""
        message = self._format_alert_message(alert, current_price)
        print(f"[{self._timestamp()}] Срабатано оповещение: {alert.coin.upper()}")
        self.on_alert(alert, current_price, message)

    def _format_alert_message(self, alert: Alert, current_price: float) -> str:
        """Форматировать сообщение об оповещении"""
        condition_text = "превысила" if alert.condition == "above" else "упала ниже"
        return (
            f"🚨 <b>Цена {alert.coin.upper()}</b>\n\n"
            f"Цена {condition_text} ${alert.price:.2f}\n"
            f"Текущая цена: ${current_price:.2f}\n\n"
            f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    @staticmethod
    def _timestamp() -> str:
        """Получить временную метку"""
        return datetime.now().strftime('%H:%M:%S')
