class House:
    name: str
    number_of_floors: int
    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int) -> None:
        def is_floor_valid(floor: int) -> bool:
            if floor < 1 or floor > self.number_of_floors:
                return False
            return True
        def move_to_floor(floor: int) -> None:
            for i in range(1, floor +1):
                print(i)

        if is_floor_valid(new_floor):
            move_to_floor(new_floor)
            return
        print("Такого этажа не существует")

def main():
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)

if __name__ == "__main__":
    main()



