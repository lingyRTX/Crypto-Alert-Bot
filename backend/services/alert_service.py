"""Сервис управления оповещениями"""
import uuid
from typing import List
from backend.models import Alert
from backend.storage import ConfigManager
from backend.api import CoingeckoAPI
from backend.telegram import TelegramBot
from backend.checker import PriceChecker


class AlertService:
    """Главный сервис для управления оповещениями"""

    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.api = CoingeckoAPI()
        self.telegram = TelegramBot(self.config.get_telegram_token())
        self.price_checker = PriceChecker(on_alert=self._on_alert_triggered)

    def initialize(self) -> None:
        """Инициализировать сервис"""
        alerts = self.config.get_alerts()
        interval = self.config.get_check_interval()
        self.price_checker.start(alerts, interval)

    def stop(self) -> None:
        """Остановить сервис"""
        self.price_checker.stop()

    def create_alert(self, coin: str, price: float, condition: str) -> Alert:
        """
        Создать новое оповещение

        Args:
            coin: ID монеты
            price: Целевая цена
            condition: "above" или "below"

        Returns:
            Созданное оповещение
        """
        alert = Alert(
            id=str(uuid.uuid4()),
            coin=coin.lower(),
            price=float(price),
            condition=condition,
            active=True
        )
        self.config.add_alert(alert)
        self.price_checker.update_alerts(self.config.get_alerts())
        return alert

    def delete_alert(self, alert_id: str) -> None:
        """Удалить оповещение"""
        self.config.remove_alert(alert_id)
        self.price_checker.update_alerts(self.config.get_alerts())

    def get_alerts(self) -> List[Alert]:
        """Получить все оповещения"""
        return self.config.get_alerts()

    def set_check_interval(self, minutes: int) -> None:
        """Установить интервал проверки"""
        self.config.set_check_interval(minutes)
        self.price_checker.check_interval = minutes

    def set_telegram_token(self, token: str) -> bool:
        """Установить и проверить токен Telegram"""
        temp_bot = TelegramBot(token)
        if temp_bot.is_valid():
            self.config.set_telegram_token(token)
            self.telegram = temp_bot
            return True
        return False

    def set_telegram_user_id(self, user_id: str) -> None:
        """Установить ID пользователя Telegram"""
        self.config.set_telegram_user_id(user_id)

    def test_telegram(self) -> bool:
        """Тестировать подключение к Telegram"""
        user_id = self.config.get_telegram_user_id()
        if not user_id:
            return False

        return self.telegram.send_message(
            user_id,
            "✅ Тестовое сообщение от CryptoAlertBot"
        )

    def get_current_price(self, coin: str) -> float:
        """Получить текущую цену монеты"""
        price = self.api.get_price(coin.lower())
        return price or 0.0

    def _on_alert_triggered(self, alert: Alert, price: float, message: str) -> None:
        """Callback при срабатывании оповещения"""
        user_id = self.config.get_telegram_user_id()
        if user_id:
            self.telegram.send_message(user_id, message)
