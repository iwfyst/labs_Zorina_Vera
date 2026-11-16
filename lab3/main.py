from singleton import GameState
from factory_method import EmailService, SmsService
from abstract_factory import InteriorRoom, LoftFurnitureFactory, ModernFurnitureFactory
from builder import ComputerBuilder, build_gaming_pc


def main():
    print("SINGLETON")
    state1 = GameState()
    state1.add_score(100)

    state2 = GameState()
    state2.next_level()

    print("state1 is state2:", state1 is state2)
    print(f"state1   Очки: {state1.score}, Уровень: {state1.level}")
    print(f"state2   Очки: {state2.score}, Уровень: {state2.level}")

    print("\nFACTORY METHOD")
    for service, target in [(EmailService(), "user@example.com"), (SmsService(), "+79123456789")]:
        print(service.notify_user(target, "Ваш заказ готов!"))

    print("\nABSTRACT FACTORY")
    print(InteriorRoom(LoftFurnitureFactory()).describe())
    print(InteriorRoom(ModernFurnitureFactory()).describe())

    print("\nBUILDER")
    custom_pc = ComputerBuilder("Apple M3", 16).add_storage("SSD 512GB").build()
    pro_pc = build_gaming_pc(ComputerBuilder("Intel Core i9", 64))
    print("Custom:", custom_pc)
    print("Gaming:", pro_pc)


if __name__ == "__main__":
    main()
