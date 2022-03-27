# Задание №1

# from time import sleep
#
#
# class TrafficLight:
#     color = ['Красный', 'Желтый', 'Зеленый']
#
#     def run(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(5)
#             elif i == 2:
#                 sleep(2)
#             i += 1
#
#
# TrafficLight = TrafficLight()
# TrafficLight.run()

# Задание №2

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def mass(self):
#         return self._length * self._width
#
#
# class MassCount(Road):
#     def __init__(self, _length, _width, volume):
#         super().__init__(_length, _width)
#         self.volume = volume
#
#
# r = MassCount(20, 5000, 25)
# print(r.mass())

# Задание №3

# class Worker():
#
#     def __init__(self, lname, fname, position, wage, bonus):
#         self.lname = lname
#         self.fname = fname
#         self.position = position
#         self.wage = wage
#         self.bonus = bonus
#         self._income = {'wage': self.wage, 'bonus':  self.wage * self.bonus / 100}
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return self.lname + ' ' + self.fname
#
#     def get_total_income(self):
#         return self._income.get('wage') +  self._income.get('bonus')
#
# w1 = Position('Иванов', 'Иван', 'электромонтер', 1000, 25)
# print('Фамилия:', w1.lname)
# print('Имя:', w1.fname)
# print('Должность:', w1.position)
# print('Полное имя:', w1.get_full_name())
# print('Оклад, руб:', w1.wage)
# print('Размер премии, %:', w1.bonus)
# print('Размер дохода, руб:', w1.get_total_income())
#
# w2 = Position('Петров', 'Петр', 'мастер', 1200, 30)
# print(w2.lname)
# print(w2.fname)
# print(w2.position)
# print(w2.get_full_name())
# print(w2.get_total_income())

# Задание №4

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} is started'
#
#     def stop(self):
#         return f'{self.name} is stopped'
#
#     def turn_right(self):
#         return f'{self.name} is turned right'
#
#     def turn_left(self):
#         return f'{self.name} is turned left'
#
#     def show_speed(self):
#         return f'Current speed {self.name} is {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Current speed of town car {self.name} is {self.speed}')
#
#         if self.speed > 40:
#             return f'Speed of {self.name} is higher than allow for town car'
#         else:
#             return f'Speed of {self.name} is normal for town car'
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Current speed of work car {self.name} is {self.speed}')
#
#         if self.speed > 60:
#             return f'Speed of {self.name} is higher than allow for work car'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} is from police department'
#         else:
#             return f'{self.name} is not from police department'
#
#
# Ferrari = SportCar(100, 'Red', 'Ferrari', False)
# Kia = TownCar(30, 'Black', 'Kia', False)
# BMW = WorkCar(70, 'Green', 'BMW', True)
# hyundai = PoliceCar(110, 'Blue',  'hyundai', True)
# print(BMW.turn_left())
# print(f'When {Kia.turn_right()}, then {Ferrari.stop()}')
# print(f'{BMW.go()} with speed exactly {BMW.show_speed()}')
# print(f'{BMW.name} is {BMW.color}')
# print(f'Is {Ferrari.name} a police car? {Ferrari.is_police}')
# print(f'Is {BMW.name}  a police car? {BMW.is_police}')
# print(Ferrari.show_speed())
# print(Kia.show_speed())
# print(hyundai.police())
# print(BMW.show_speed())

# Задание №5

# class Stationary:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
#
# class Pen(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки ручкой'
#
#
# class Pencil(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки карандашом'
#
#
# class Handle(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки маркером'
#
#
# pen = Pen('Ручка')
# pencil = Pencil('Карандаш')
# handle = Handle('Маркер')
# print(pen.draw())
# print(pencil.draw())
# print(handle.draw())
