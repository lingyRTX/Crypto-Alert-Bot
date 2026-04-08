"""API клиент для Coingecko"""
import requests
from typing import Optional, Dict


class CoingeckoAPI:
    """Клиент для получения цен из Coingecko API"""

    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(self):
        self.session = requests.Session()
        self.session.timeout = 10

    def get_price(self, coin_id: str, vs_currency: str = "usd") -> Optional[float]:
        """
        Получить текущую цену криптовалюты

        Args:
            coin_id: ID монеты (bitcoin, ethereum, ripple, etc.)
            vs_currency: Валюта для сравнения (по умолчанию USD)

        Returns:
            Цена или None если ошибка
        """
        try:
            url = f"{self.BASE_URL}/simple/price"
            params = {
                "ids": coin_id.lower(),
                "vs_currencies": vs_currency.lower()
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            if coin_id.lower() in data:
                return data[coin_id.lower()].get(vs_currency.lower())
            return None
        except requests.RequestException as e:
            print(f"Ошибка API: {e}")
            return None

    def get_prices_multiple(self, coin_ids: list, vs_currency: str = "usd") -> Dict[str, float]:
        """
        Получить цены нескольких криптовалют за раз

        Args:
            coin_ids: Список ID монет
            vs_currency: Валюта для сравнения

        Returns:
            Словарь {coin_id: price}
        """
        try:
            url = f"{self.BASE_URL}/simple/price"
            params = {
                "ids": ",".join([c.lower() for c in coin_ids]),
                "vs_currencies": vs_currency.lower()
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            result = {}
            for coin_id in coin_ids:
                if coin_id.lower() in data:
                    result[coin_id] = data[coin_id.lower()].get(vs_currency.lower())
            return result
        except requests.RequestException as e:
            print(f"Ошибка API: {e}")
            return {}

    def is_available(self) -> bool:
        """Проверить доступность API"""
        try:
            url = f"{self.BASE_URL}/ping"
            response = self.session.get(url, timeout=5)
            return response.status_code == 200
        except:
            return False
