from chain import AuditApprover, LimitApprover
from iterator import Book, BookShelf, ReverseBookIterator
from strategy import NoDiscount, PercentageDiscount, ShoppingCart, ThresholdDiscount


def run_strategy_demo() -> None:
    print("1. ПАТТЕРН СТРАТЕГИЯ")
    cart = ShoppingCart(total_amount=5000.0, strategy=NoDiscount())
    print(f"Без скидки: {cart.checkout()} руб.")

    cart.strategy = PercentageDiscount(15)
    print(f"Скидка 15%: {cart.checkout()} руб.")

    cart.strategy = ThresholdDiscount(threshold=4000.0, bonus=700.0)
    print(f"Бонус 700 руб. от 4000 руб.: {cart.checkout()} руб.\n")


def run_chain_demo() -> None:
    print("2. ЦЕПОЧКА ОБЯЗАННОСТЕЙ (CHAIN OF RESPONSIBILITY)")
    lead = LimitApprover("Тимлид", limit=15_000)
    head = LimitApprover("Руководитель отдела", limit=100_000)
    audit = AuditApprover(max_allowed_without_board=300_000)
    director = LimitApprover("Финансовый директор", limit=500_000)

    lead.set_next(head).set_next(audit).set_next(director)

    for expense in (8_000, 45_000, 250_000, 325_000, 1_200_000):
        print(lead.handle(expense))
    print()


def run_iterator_demo() -> None:
    print("3. ПАТТЕРН ИТЕРАТОР (ITERATOR)")
    shelf = BookShelf()
    shelf.add_book(Book("Чистый код", "Роберт Мартин"))
    shelf.add_book(Book("Совершенный код", "Стив Макконнелл"))
    shelf.add_book(Book("Паттерны ООП", "GoF"))

    print("Прямой обход (по умолчанию):")
    for book in shelf:
        print(f"  - {book.title} ({book.author})")

    print("\nНезависимый обратный обход через два итератора:")
    rev1 = shelf.custom_iter(ReverseBookIterator)
    rev2 = shelf.custom_iter(ReverseBookIterator)

    print("  Итератор 1, шаг 1:", next(rev1))
    print("  Итератор 1, шаг 2:", next(rev1))
    print("  Итератор 2, шаг 1:", next(rev2))


if __name__ == "__main__":
    run_strategy_demo()
    run_chain_demo()
    run_iterator_demo()
