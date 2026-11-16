## система уведомлений
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, text: str) -> str:
        pass

class EmailNotifier(Notifier):
    def send(self, recipient: str, text: str) -> str:
        return f"Email на {recipient}: {text}"

class SmsNotifier(Notifier):
    def send(self, recipient: str, text: str) -> str:
        return f"SMS на номер {recipient}: {text}"


class NotificationService(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        pass

    def notify_user(self, recipient: str, message: str) -> str:
        formatted_text = f"[Уведомление] {message}"
        notifier = self.create_notifier()
        return notifier.send(recipient, formatted_text)

class EmailService(NotificationService):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()

class SmsService(NotificationService):
    def create_notifier(self) -> Notifier:
        return SmsNotifier()


if __name__ == "__main__":
    email_sender = EmailService()
    print(email_sender.notify_user("student@misis.ru", "Лабораторная принята"))

    sms_sender = SmsService()
    print(sms_sender.notify_user("+79991234567", "Ваш код подтверждения: 4815"))
