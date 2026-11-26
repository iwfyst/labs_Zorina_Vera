from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class CurrencyConverter(ABC):
    @abstractmethod
    def convert_to_rub(self, amount: float, currency: str) -> float:
        pass


class LegacyXmlRatesService:
    def fetch_rate_xml(self, xml_request: str) -> str:
        root = ET.fromstring(xml_request)
        currency = root.find("currency").text
        rates = {"USD": 90.0, "EUR": 98.5}
        rate = rates.get(currency, 1.0)
        return f"<response><rate>{rate}</rate></response>"


class XmlRatesAdapter(CurrencyConverter):
    def __init__(self, legacy_service: LegacyXmlRatesService):
        self._legacy_service = legacy_service

    def convert_to_rub(self, amount: float, currency: str) -> float:
        xml_payload = f"<request><currency>{currency}</currency></request>"
        xml_response = self._legacy_service.fetch_rate_xml(xml_payload)
        root = ET.fromstring(xml_response)
        rate = float(root.find("rate").text)
        return round(amount * rate, 2)


def run_adapter_demo() -> None:
    print("ПАТТЕРН ADAPTER")
    legacy_api = LegacyXmlRatesService()
    converter: CurrencyConverter = XmlRatesAdapter(legacy_api)

    usd_amount = 100.0
    rub_amount = converter.convert_to_rub(usd_amount, "USD")
    print(f"Конвертация {usd_amount} USD -> {rub_amount} RUB\n")


if __name__ == "__main__":
    run_adapter_demo()
