import math
class Figure:
    sides_count: int = 0

    def __init__(self, color: tuple[int, int, int], *sides) -> None:
        is_color_valid = self.set_color(*color)
        # is_sides_valid = self.set_sides(*sides)
        if self.__is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            init_sides: list = []
            for _ in range(self.sides_count):
                init_sides.append(1)
            self.__sides = tuple(init_sides)
        if not is_color_valid:
            print('Invalid params input!')
            raise Exception()
        self.__color: tuple[int, int, int] = color
        # self.filled: bool = filled
        self.filled: bool = True

    def get_color(self) -> list[int]:
        return list(self.__color)

    def __is_valid_color(self, color: tuple[int, int, int]) -> bool:
        is_valid: bool = True
        for color_type in color:
            is_valid = is_valid and (color_type >=0 and color_type <=255)
        return is_valid

    def set_color(self, r: int, g: int, b: int) -> bool:
        new_color = (r, g, b)
        if self.__is_valid_color(new_color):
            self.__color = new_color
            return True
        return False

    def __is_valid_sides(self, *sides_to_check) -> bool:
        if len(sides_to_check) != self.sides_count:
            return False
        for side in sides_to_check:
            if side <= 0:
                return False
        return True

    def get_sides(self) -> list[float]:
        return list(self.__sides)

    # have to return int to work with len()
    def __len__(self) -> int:
        return int(sum(self.__sides))

    def _set_equal_sides(self, side: float) -> None:
        new_sides_list: list[float] = []
        for _ in range(self.sides_count):
            new_sides_list.append(side)
        self.__sides = tuple(new_sides_list)

    def __sides_on_creation(self, *new_sides) -> None:
        pass

    def set_sides(self, *new_sides) -> bool:
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
            return True
        # self._set_equal_sides(1)
        return False



class Circle(Figure):
    sides_count: int = 1
    __radius: float

    def __init__(self, color: tuple[int, int, int], *sides) -> None:
        super().__init__(color, *sides)
        self.__radius = self.__calc_radius(sides[0])

    def __calc_radius(self, side_length: float) -> float:
        return (side_length/(2*math.pi))

    def get_square(self) -> float:
        radius = self.__radius
        return (radius * radius * math.pi)

class Triangle(Figure):
    sides_count: int = 3

    def get_square(self) -> float:
        half_per: float = len(self) / 2
        a: float = half_per - self.__sides[0]
        b: float = half_per - self.__sides[1]
        c: float = half_per - self.__sides[2]
        return math.sqrt(half_per*a*b*c)

class Cube(Figure):
    sides_count: int = 12

    def __init__(self, color: tuple[int, int, int], *sides) -> None:
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.side_length = sides[0]
            self._set_equal_sides(self.side_length)
        else:
            self.side_length = 1 
            self._set_equal_sides(1)

    def get_volume(self) -> float:
        side = self.side_length
        return side*side*side



def main():
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())
    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    # Проверка объёма (куба):
    print(cube1.get_volume())



if __name__ == "__main__":
    main()
