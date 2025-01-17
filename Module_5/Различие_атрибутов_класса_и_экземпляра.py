class House:
    houses_history = []
    name: str
    floors: int
    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name: str, floors: int) -> None:
        self.name = name
        self.floors = floors

    def __del__ (self) -> None:
        print(f"{self.name} снесен, но останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)





