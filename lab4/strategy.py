#расчёт скидки в корзине
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Сумма заказа не может быть отрицательной.")
        return amount


class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return super().apply_discount(amount)


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Процент скидки должен быть от 0 до 100.")
        self._percent = percent

    def apply_discount(self, amount: float) -> float:
        valid_amount = super().apply_discount(amount)
        return round(valid_amount * (1 - self._percent / 100), 2)


class ThresholdDiscount(DiscountStrategy):
    def __init__(self, threshold: float, bonus: float):
        if threshold < 0 or bonus < 0:
            raise ValueError("Порог и размер бонуса должны быть неотрицательными.")
        self._threshold = threshold
        self._bonus = bonus

    def apply_discount(self, amount: float) -> float:
        valid_amount = super().apply_discount(amount)
        if valid_amount >= self._threshold:
            return round(max(0.0, valid_amount - self._bonus), 2)
        return valid_amount


class ShoppingCart:

    def __init__(self, total_amount: float, strategy: DiscountStrategy):
        if total_amount < 0:
            raise ValueError("Сумма корзины не может быть отрицательной.")
        self.total_amount = total_amount
        self.strategy = strategy

    def checkout(self) -> float:
        return self.strategy.apply_discount(self.total_amount)

