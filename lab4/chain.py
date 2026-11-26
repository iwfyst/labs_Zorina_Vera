#согласование заявки на закупку
from abc import ABC, abstractmethod
from typing import Optional


class Approver(ABC):

    def __init__(self, role_name: str, limit: int, next_approver: Optional["Approver"] = None):
        self._role_name = role_name
        self._limit = limit
        self._next = next_approver

    def set_next(self, next_approver: "Approver") -> "Approver":
        self._next = next_approver
        return next_approver

    def handle(self, amount: int) -> str:
        if amount <= 0:
            raise ValueError("Сумма заявки должна быть положительной.")
        if self._can_approve(amount):
            return f"{self._role_name} одобрил заявку на {amount} руб."
        if self._next is not None:
            return self._next.handle(amount)
        return f"Заявка на {amount} руб. отклонена: превышен максимальный лимит."

    @abstractmethod
    def _can_approve(self, amount: int) -> bool:
        pass


class LimitApprover(Approver):

    def _can_approve(self, amount: int) -> bool:
        return amount <= self._limit


class AuditApprover(Approver):

    def __init__(self, max_allowed_without_board: int, next_approver: Optional[Approver] = None):
        super().__init__("Комитет по аудиту", max_allowed_without_board, next_approver)

    def _can_approve(self, amount: int) -> bool:
        # Одобряет только круглые суммы в пределах лимита
        return amount <= self._limit and amount % 10_000 == 0

