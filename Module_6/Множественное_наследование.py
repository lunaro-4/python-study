import random
class Animal:
    live: bool = True
    sound: str | None = None
    _DEGREE_OF_DANGER: int = 0

    def __init__(self, speed: int) -> None:
        self._coords: list[float] = [0, 0, 0]
        self.speed = speed

    def move(self, dx: float, dy: float, dz: float) -> None:
        x = dx * self.speed
        y = dy * self.speed
        z = dz * self.speed
        if z < 0 :
            print("It's too deep, I can't dive :(")
            return
        self._coords = [self._coords[0] + x, self._coords[1] + y, self._coords[2] + z]
    def get_cords(self) -> None:
        x, y, z = self._coords[0], self._coords[1], self._coords[2]
        print("X: %2i\tY: %2i\tZ: %2i" %  (x, y, z) )

    def attack(self) -> None:
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")
    def speak(self) -> None:
        print(self.sound)

class Bird(Animal):
    beak: bool = True
    def lay_eggs(self) -> None:
        eggs = int(random.random() * 4)+1
        print(f"Here are(is) {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz: float) -> None:
        self._coords[2] -= abs(dz) * (self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal ):

    def __init__(self, speed: int) -> None:
        super().__init__(speed)
        self.sound = "Click-click-click"

db = Duckbill(10)



print(db.live)

print(db.beak)



db.speak()

db.attack()



db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()



db.lay_eggs()


