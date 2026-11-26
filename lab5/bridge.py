from abc import ABC, abstractmethod


class MessageChannel(ABC):
    @abstractmethod
    def deliver(self, formatted_text: str) -> str:
        pass


class SmsChannel(MessageChannel):
    def deliver(self, formatted_text: str) -> str:
        return f"[SMS-шлюз] Отправлено: {formatted_text}"


class PushChannel(MessageChannel):
    def deliver(self, formatted_text: str) -> str:
        return f"[Push-сервер] Уведомление: {formatted_text}"


class BankNotification(ABC):
    def __init__(self, channel: MessageChannel):
        self._channel = channel

    @abstractmethod
    def send(self, details: str) -> str:
        pass


class ReceiptNotification(BankNotification):
    def send(self, details: str) -> str:
        text = f"Чек по операции: {details}"
        return self._channel.deliver(text)


class FraudAlertNotification(BankNotification):
    def send(self, details: str) -> str:
        text = f"ВНИМАНИЕ! Подозрительная активность: {details}"
        return self._channel.deliver(text)


def run_bridge_demo() -> None:
    print("ПАТТЕРН BRIDGE")
    sms = SmsChannel()
    push = PushChannel()

    receipt_via_sms = ReceiptNotification(sms)
    alert_via_push = FraudAlertNotification(push)
    alert_via_sms = FraudAlertNotification(sms)

    print(receipt_via_sms.send("Оплата кофе 350 руб."))
    print(alert_via_push.send("Вход с нового устройства"))
    print(alert_via_sms.send("Попытка списания 90 000 руб."))
    print()


if __name__ == "__main__":
    run_bridge_demo()
