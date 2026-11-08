from abc import ABC, abstractmethod


class Moveable(ABC):
    @abstractmethod
    def move(self, new_x: int, new_y: int) -> None:
        pass


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit: 'Unit') -> None:
        pass


class GameObject(ABC):
    def __init__(self, id_obj: int, name: str, x: int, y: int):
        self._id = id_obj
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int: return self._id

    def get_name(self) -> str: return self._name

    def get_x(self) -> int: return self._x

    def get_y(self) -> int: return self._y


class Unit(GameObject):
    def __init__(self, id_obj: int, name: str, x: int, y: int, hp: float):
        super().__init__(id_obj, name, x, y)
        self._hp = hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float) -> None:
        if not self.is_alive(): return
        self._hp -= damage
        if self._hp < 0: self._hp = 0.0
        print(f"[{self._name}] получил {damage} урона. Осталось HP: {self._hp}")


class Building(GameObject):
    def __init__(self, id_obj: int, name: str, x: int, y: int, is_built: bool = False):
        super().__init__(id_obj, name, x, y)
        self._is_built = is_built

    def is_built(self) -> bool: return self._is_built


class Archer(Unit, Attacker, Moveable):
    def __init__(self, id_obj: int, name: str, x: int, y: int, hp: float, damage: float):
        super().__init__(id_obj, name, x, y, hp)
        self._damage = damage

    def move(self, new_x: int, new_y: int) -> None:
        if not self.is_alive(): return
        self._x = new_x
        self._y = new_y
        print(f"Лучник {self._name} переместился в ({self._x}, {self._y})")

    def attack(self, unit: Unit) -> None:
        if not self.is_alive() or not unit.is_alive(): return
        print(f"Лучник {self._name} атакует {unit.get_name()}!")
        unit.receive_damage(self._damage)


class Fort(Building, Attacker):
    def __init__(self, id_obj: int, name: str, x: int, y: int, is_built: bool, damage: float):
        super().__init__(id_obj, name, x, y, is_built)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.is_built() or not unit.is_alive(): return
        print(f"Крепость {self._name} атакует {unit.get_name()}!")
        unit.receive_damage(self._damage)


class MobileHouse(Building, Moveable):
    def move(self, new_x: int, new_y: int) -> None:
        self._x = new_x
        self._y = new_y
        print(f"Дом на колесах {self._name} переехал в ({self._x}, {self._y})")


if __name__ == "__main__":
    player = Archer(1, "Игрок", 0, 0, 100.0, 25.0)
    boss = Unit(2, "Босс", 5, 5, 60.0)
    fort = Fort(3, "Цитадель", 10, 10, True, 50.0)

    player.move(3, 3)
    player.attack(boss)
    fort.attack(boss)
