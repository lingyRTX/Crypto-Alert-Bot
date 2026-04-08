"""Модель оповещения о цене"""
from dataclasses import dataclass, asdict
from typing import Literal


@dataclass
class Alert:
    """Класс для хранения данных об оповещении"""
    id: str
    coin: str  # bitcoin, ethereum, etc.
    price: float  # целевая цена
    condition: Literal["above", "below"]  # выше или ниже цены
    active: bool = True

    def to_dict(self) -> dict:
        """Конвертировать в словарь"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'Alert':
        """Создать из словаря"""
        return cls(**data)
