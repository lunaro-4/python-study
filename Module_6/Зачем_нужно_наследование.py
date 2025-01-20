class Plant:
    edible: bool = True
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

class Animal:
    alive: bool = True
    fed: bool = False
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self, food: Plant) -> None:
        if not food.edible:
            self.alive = False
        else:
            self.fed = True



class Mammal(Animal):
    def eat(self, food) -> None:
        super().eat(food)
        if isinstance(food, Plant):
            print(f"{self.name} съел {food.name}")

class Predator(Animal):
    def eat(self, food) -> None:
        super().eat(food)
        if isinstance(food, Plant):
            print(f"{self.name} не стал есть {food.name}")

class Flower(Plant):
    edible: bool = False

class Fruit(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

