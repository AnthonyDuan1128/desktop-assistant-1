import requests

class CurrencyService:
    def __init__(self):
        self.exchange_rates = {}
        self.api_key = "657d7c82a8c4147c49961298"
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/"

    def fetch_exchange_rates(self, base_currency="USD"):
        url = f"{self.base_url}{base_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.exchange_rates = data['conversion_rates']
        else:
            raise Exception("Failed to fetch exchange rates")

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Currency not supported")
        return amount * (self.exchange_rates[to_currency] / self.exchange_rates[from_currency])