class House:
    name: str
    number_of_floors: int

    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self) -> str:
        return f"Название:  {self.name},    кол-во этажей:  {self.number_of_floors}"

    def __add_floors(self, value: int) -> None:
        self.number_of_floors += value
    def __add__(self, value: int):
        self.__add_floors(value)
        return self
    def __radd__(self, value: int):
        self.__add_floors(value)
        return self
    def __iadd__(self, value: int):
        self.__add_floors(value)
        return self

    def __eq__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors == other.number_of_floors

    def __gt__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other) -> bool:
        if not isinstance(other, House):
            return False
        return self.number_of_floors != other.number_of_floors




def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    print(h1)
    print(h2)
    print(h1 == h2) # __eq__
    h1 = h1 + 10 # __add__
    print(h1)
    print(h1 == h2)
    h1 += 10 # __iadd__
    print(h1)
    h2 = 10 + h2 # __radd__
    print(h2)
    print(h1 > h2) # __gt__
    print(h1 >= h2) # __ge__
    print(h1 < h2) # __lt__
    print(h1 <= h2) # __le__
    print(h1 != h2) # __ne__

if __name__ == "__main__":
    main()

