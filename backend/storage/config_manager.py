"""Управление конфигурацией и оповещениями"""
import json
import os
from typing import List
from pathlib import Path
from backend.models import Alert


class ConfigManager:
    """Менеджер для работы с config.json"""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """Загрузить конфигурацию из файла"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return self._get_default_config()

    def _get_default_config(self) -> dict:
        """Получить конфигурацию по умолчанию"""
        return {
            "telegram_token": "",
            "telegram_user_id": "",
            "check_interval": 5,
            "alerts": []
        }

    def save_config(self) -> None:
        """Сохранить конфигурацию в файл"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def get_telegram_token(self) -> str:
        """Получить токен Telegram бота"""
        return self.config.get("telegram_token", "")

    def set_telegram_token(self, token: str) -> None:
        """Установить токен Telegram бота"""
        self.config["telegram_token"] = token
        self.save_config()

    def get_telegram_user_id(self) -> str:
        """Получить ID пользователя Telegram"""
        return self.config.get("telegram_user_id", "")

    def set_telegram_user_id(self, user_id: str) -> None:
        """Установить ID пользователя Telegram"""
        self.config["telegram_user_id"] = str(user_id)
        self.save_config()

    def get_check_interval(self) -> int:
        """Получить интервал проверки в минутах"""
        return self.config.get("check_interval", 5)

    def set_check_interval(self, minutes: int) -> None:
        """Установить интервал проверки в минутах"""
        if 1 <= minutes <= 60:
            self.config["check_interval"] = minutes
            self.save_config()

    def get_alerts(self) -> List[Alert]:
        """Получить все оповещения"""
        alerts_data = self.config.get("alerts", [])
        return [Alert.from_dict(a) for a in alerts_data]

    def add_alert(self, alert: Alert) -> None:
        """Добавить новое оповещение"""
        if "alerts" not in self.config:
            self.config["alerts"] = []
        self.config["alerts"].append(alert.to_dict())
        self.save_config()

    def remove_alert(self, alert_id: str) -> None:
        """Удалить оповещение по ID"""
        self.config["alerts"] = [
            a for a in self.config["alerts"]
            if a.get("id") != alert_id
        ]
        self.save_config()

    def update_alert(self, alert: Alert) -> None:
        """Обновить существующее оповещение"""
        for i, a in enumerate(self.config["alerts"]):
            if a.get("id") == alert.id:
                self.config["alerts"][i] = alert.to_dict()
                self.save_config()
                break
