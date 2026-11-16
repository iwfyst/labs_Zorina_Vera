## менеджер состояния игры
class GameState:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            obj = super().__new__(cls)
            obj.score = 0
            obj.level = 1
            cls._instance = obj
        return cls._instance
    def add_score(self, points: int):
        self.score += points
    def next_level(self):
        self.level += 1

if __name__ == "__main__":
    state1 = GameState()
    state1.add_score(100)

    state2 = GameState()
    state2.next_level()

    print("Один и тот же объект:", state1 is state2)
    print(f"Очки: {state1.score}, Уровень: {state1.level}")
    print(f"Очки: {state2.score}, Уровень: {state2.level}")