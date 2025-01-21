class Vehicle:
    __COLOR_VARIANTS: list[str] = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, horsepower: int) -> None:
        if not self.set_color(color):
            print('Не удалось создать машину в этой кофигурации')
            return
        self.owner = owner
        self.__model = model
        self.__engine_power = horsepower
        
        

    def get_model(self) -> str:
        return self.__model
    def get_horsepower(self) -> int:
        return self.__engine_power
    def get_color(self) -> str:
        return self.__color
    def print_info(self) -> None:
        print(f"""Модель: {self.get_model()}
Мощность двигателя: {self.get_horsepower()}
Цвет: {self.get_color()}
Владелец: {self.owner} """)
    def __is_valid_color(self, color_to_check: str) -> bool:
        for color in self.__COLOR_VARIANTS:
            if color.casefold() == color_to_check.casefold():
                return True
        return False

    def set_color(self, new_color: str) -> bool:
        if self.__is_valid_color(new_color):
            self.__color = new_color
            return True
        print(f'Нельзя сменить цвет на {new_color}')
        return False

class Sedan(Vehicle):
    __PASSENGERS_LIMIT: int = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()
