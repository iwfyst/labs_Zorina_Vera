## машазин мебели
from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass

class Table(ABC):
    @abstractmethod
    def put_items(self) -> str:
        pass


class LoftChair(Chair):
    def sit_on(self) -> str:
        return "Металлический стул в стиле Лофт"

class LoftTable(Table):
    def put_items(self) -> str:
        return "Деревянный стол в стиле Лофт"


class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Минималистичный стул в стиле Модерн"


class ModernTable(Table):
    def put_items(self) -> str:
        return "Стеклянный стол в стиле Модерн"


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class LoftFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return LoftChair()

    def create_table(self) -> Table:
        return LoftTable()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


class InteriorRoom:
    def __init__(self, factory: FurnitureFactory):
        self.chair = factory.create_chair()
        self.table = factory.create_table()

    def describe(self) -> str:
        return f"В комнате стоят: {self.chair.sit_on()} и {self.table.put_items()}."


if __name__ == "__main__":
    loft_room = InteriorRoom(LoftFurnitureFactory())
    print(loft_room.describe())

    modern_room = InteriorRoom(ModernFurnitureFactory())
    print(modern_room.describe())
