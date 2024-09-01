class Vechicle():
    def __init__(self, owner, __model, __color, __en_pow):
        self.owner=owner
        self.__model=__model
        if isinstance(__en_pow, int):
            self.__en_pow=__en_pow
        self.__color=__color
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        print(f'Модель: {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__en_pow}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__en_pow}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        for i in range(len(self.__COLOR_VARIANTS)):
            n=new_color.lower()
            a=False
            if n==self.__COLOR_VARIANTS[i].lower():
                self.__color=new_color
                a=True
        if a==False:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vechicle):
    __PASSENGERS_LIMIT=5
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
