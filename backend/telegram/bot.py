"""Telegram бот для отправки уведомлений"""
import requests
from typing import Optional


class TelegramBot:
    """Клиент для отправки сообщений в Telegram"""

    BASE_URL = "https://api.telegram.org/bot"

    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()

    def send_message(self, chat_id: str, message: str) -> bool:
        """
        Отправить сообщение в Telegram

        Args:
            chat_id: ID чата или пользователя
            message: Текст сообщения

        Returns:
            True если успешно, False если ошибка
        """
        try:
            url = f"{self.BASE_URL}{self.token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "HTML"
            }
            response = self.session.post(url, json=payload, timeout=10)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Ошибка Telegram: {e}")
            return False

    def is_valid(self) -> bool:
        """Проверить валидность токена"""
        try:
            url = f"{self.BASE_URL}{self.token}/getMe"
            response = self.session.get(url, timeout=5)
            return response.status_code == 200
        except:
            return False
