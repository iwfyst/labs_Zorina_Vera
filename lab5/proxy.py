from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def transfer(self, amount: float, recipient: str) -> str:
        pass


class RealPaymentService(PaymentProcessor):
    def transfer(self, amount: float, recipient: str) -> str:
        return f"[BankCore] Перевод {amount} руб. для {recipient} успешно выполнен."


class ProtectedPaymentService(PaymentProcessor):
    def __init__(self, real_service: PaymentProcessor, user_role: str):
        self._real_service = real_service
        self._user_role = user_role

    def transfer(self, amount: float, recipient: str) -> str:
        if self._user_role != "ADMIN":
            return f"[Proxy: Отказ] Роль '{self._user_role}' не имеет прав на перевод {amount} руб."
        return self._real_service.transfer(amount, recipient)


def run_proxy_demo() -> None:
    print("ПАТТЕРН PROXY")
    core_service = RealPaymentService()

    guest_proxy: PaymentProcessor = ProtectedPaymentService(core_service, user_role="GUEST")
    admin_proxy: PaymentProcessor = ProtectedPaymentService(core_service, user_role="ADMIN")

    print(guest_proxy.transfer(5000.0, "Иван И."))
    print(admin_proxy.transfer(5000.0, "Иван И."))
    print()


if __name__ == "__main__":
    run_proxy_demo()
