# Задание №1
#
# from random import randint as rnd
#
# class data_convert():
#     def __init__(self, str_date):
#         self.str_date = str_date
#         self.dd, self.mm, self.yy = self.get_data_components(self.str_date)
#
#     def __str__(self):
#         return self.check_data_components(self.dd, self.mm, self.yy)
#
#     @staticmethod
#     def check_data_components(dd, mm, yy):
#         ret_val = True
#         print(f'\nДата на входе в функцию: {dd:02d}-{mm:02d}-{yy:04d}')
#
#         is_leap = False
#         if yy % 4 == 0 and yy % 400 == 0 and yy % 100 != 0:
#             is_leap = True
#
#         if yy < 1800 or yy > 2200:
#             print(f'Некорректный номер года {yy:04d}')
#             ret_val = False
#
#         if mm > 12:
#             print(f'Некорректный номер месяца {mm:02d}')
#             ret_val = False
#
#         if mm in (1, 3, 5, 7, 8, 10, 12):
#             max_dd = 31
#         elif mm == 2:
#             if is_leap:
#                 max_dd = 29
#             else:
#                 max_dd = 28
#         else:
#             max_dd = 30
#
#         if dd > max_dd:
#             print(f'Некорректный номер дня {dd:02d} для месяца {mm:02d}')
#             ret_val = False
#
#         if ret_val:
#             return 'Корректная дата'
#         else:
#             return 'Некорректная дата'
#
#     @classmethod
#     def get_data_components(cls, str_data):
#         data_list = str_data.split('-')
#         return (int(data_list[i]) for i in range(len(data_list)))
#
#
# d1 = data_convert('32-13-2400')
# print(d1)
#
#
# print('\nПроверка работы класса через создание экземпляра класса')
# for i in range(20):
#     dd = rnd(1, 33)
#     mm = rnd(1, 15)
#     yy = rnd(1700, 2300)
#     d1 = data_convert(str(dd) + '-' + str(mm) + '-' + str(yy))
#     print(d1)
#
#
# print('\nПроверка работы класса с использованием @staticmethod')
# for i in range(20):
#     dd = rnd(1, 32)
#     mm = rnd(1, 13)
#     yy = rnd(1700, 2300)
#     print(data_convert.check_data_components(dd, mm, yy))

# Задание №2

# class DivisionByNull:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Деление на ноль недопустимо")
#
#
# div = DivisionByNull(10, 100)
# print(DivisionByNull.divide_by_null(10, 5))
# print(DivisionByNull.divide_by_null(10, 0.1))
# print(div.divide_by_null(100, 0))

# Задание №3

# class Error:
#     def __init__(self, *args):
#         self.list = []
#
#     def new_input(self):
#         while True:
#
#             try:
#                 val = int(input('Введите число '))
#                 self.list.append(val)
#                 print(f'Текущий список - {self.list} \n ')
#             except:
#                 print("Вы ввели не число!")
#                 decision = input("если хотите закончить, напишите stop, иначе продолжим ")
#                 if decision == "stop":
#                     return "конец"
#                 else:
#                     print(try_except.new_input())
#
#
# try_except = Error(1)
# print(try_except.new_input())

# Задание №4

# import shop
#
# dev1 = shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000)
# dev1.info()
#
# dev2 = shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm')
# dev2.info()
#
# dev3 = shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm')
# dev3.info()

# Задание №5

# import shop
#
# s1 = shop.store(1, 'Основной склад', 'ул. Ленина, 1', 'Иванов И.И.', {})
# s1.store_info()
#
# s2 = shop.store(2, 'Магазин-1', 'ул. Московская, 1', 'Петров П.П.', {})
# s2.store_info()
#
# s3 = shop.store(3, 'Магазин-2', 'ул. Ломоносова, 1', 'Сидоров С.С.', {})
# s3.store_info()
#
# dev1 = shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000)
# #dev1.info()
#
# dev2 = shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm')
# #dev2.info()
#
# dev3 = shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm')
# #dev3.info()
#
# s1.move_dev('in', {dev1: 2, dev2: 4, dev3:5})
# s1.print_dev_count()
# s1.move_dev('in', {dev2: 1, dev3: 1, dev1: 2})
# s1.print_dev_count()
#
# s2.move_dev('in', {dev1: 1, dev2: 1, dev3:1})
# s2.print_dev_count()
#
# s3.move_dev('in', {dev2: 2, dev3: 2, dev1: 2})
# s3.print_dev_count()
#
# # перемещение товара между складами:
# s1.move_dev('out', {dev1: 1, dev2: 2, dev3: 5})
# s2.move_dev('in', {dev1: 1, dev2: 2, dev3: 5})
# s1.print_dev_count()
# s2.print_dev_count()

# Задание №6

# import shop
#
# store_lst = []
# dev_lst = []
#
# store_lst.append(shop.store(1, 'Основной склад', 'ул. Ленина, 1', 'Иванов И.И.', {}))
# store_lst.append(shop.store(2, 'Магазин-1', 'ул. Московская, 1', 'Петров П.П.', {}))
# store_lst.append(shop.store(3, 'Магазин-2', 'ул. Ломоносова, 1', 'Сидоров С.С.', {}))
# dev_lst.append(shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000))
# dev_lst.append(shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm'))
# dev_lst.append(shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm'))
# print('Выполняем заполнение складов остатками товара')
# store_lst[0].move_dev('in', {dev_lst[0]: 2, dev_lst[1]: 4, dev_lst[2]: 5})
# store_lst[0].move_dev('in', {dev_lst[1]: 1, dev_lst[2]: 1, dev_lst[0]: 2})
# store_lst[1].move_dev('in', {dev_lst[0]: 1, dev_lst[1]: 1, dev_lst[2]: 1})
# store_lst[2].move_dev('in', {dev_lst[1]: 2, dev_lst[2]: 2, dev_lst[0]: 2})
#
# def check_store(store_id):
#     # проверка пользовательского ввода номера склада
#     store = None
#     for i in store_lst:
#         if i.store_id == store_id:
#             store = i
#             break
#
#     return store
#
#
# def print_store_list():
#     for i, store in enumerate(store_lst):
#         print(f'{i+1}. {store.store_name}')
#
#
# def get_store(msg):
#     print(msg)
#     print_store_list()
#     store_id = input('Введите id склада (пустую строку для отмены операции): ')
#
#     store = None
#     try:
#         store_id = int(store_id)
#     except ValueError:
#         print('Введено не числовое значение либо пустая строка!')
#     else:
#         store = check_store(store_id)
#         if not store:
#             print('В списке складов отсутствует введенное значение!')
#
#     return store
#
# def get_dev_by_id(dev_id):
#     # проверка пользовательского ввода id товара
#     dev = None
#     for i in dev_lst:
#         if i.id == dev_id:
#             dev = i
#             break
#
#     return dev
#
#
# def parse_dev_count(store, str_dev_count):
#     dev_count = {}
#
#     try:
#         # разбиваем строку  с количеством товара на отдельные позиции
#         lst1 = str_dev_count.split(',')
#     except:
#         print(f'Ошибка при обработке введенной строки: {str_dev_count}')
#     else:
#         for i in lst1:
#             try:
#                 # разбиваем каждую позицию на id товара и количество
#                 parse_dev_id, parse_dev_count = i.split(' ')
#                 parse_dev_id = int(parse_dev_id)
#                 parse_dev_count = int(parse_dev_count)
#             except:
#                 print(f'Ошибка при обработке введенной подстроки: {i}, будет проигнорирована!')
#             else:
#                 # записываем в возвращаемый словарь из пользовательского ввода количество по каждой позиции
#                 dev = get_dev_by_id(parse_dev_id)
#                 if not dev:
#                     print(f'Товар с id = {parse_dev_id} не найден в справочнике, будет проигнорирован!')
#                 else:
#                     dev_count[dev] = parse_dev_count
#
#     return dev_count
#
#
# while True:
#     from_store = None
#     to_store = None
#     dev_count = None
#
#     from_store = get_store('\nДля операции перемещения товара выберите склад-источник: ')
#     if not from_store:
#         print('Операция отменена!')
#         break
#
#     to_store = get_store('\nВыберите склад-получатель: ')
#     if not to_store:
#         print('Операция отменена!')
#         break
#
#     from_store.print_dev_count()
#     str_dev_count = input('Введите через запятую количество перемещаемого товара в формате: <№ товара><пробел><количество>: ')
#
#     dev_count = parse_dev_count(from_store, str_dev_count)
#     if len(dev_count) == 0:
#         print('Не удалось распознать введенную строку!')
#     else:
#         if from_store.check_count(dev_count):
#             from_store.move_dev('out', dev_count)
#             to_store.move_dev('in', dev_count)
#             print('Операция перемещения товара выполнена. Остатки товара на складах после перемещения:')
#             from_store.print_dev_count()
#             to_store.print_dev_count()
#         else:
#             print('Операция перемещения товаров не выполнена!')

# Задание №7

# class ComplexNumber:
#     def __init__(self, a, b, *args):
#         self.a = a
#         self.b = b
#         self.z = 'a + b * i'
#
#     def __add__(self, other):
#         print(f'Сумма z1 и z2 равна')
#         return f'z = {self.a + other.a} + {self.b + other.b} * i'
#
#     def __mul__(self, other):
#         print(f'Произведение z1 и z2 равно')
#         return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'
#
#     def __str__(self):
#         return f'z = {self.a} + {self.b} * i'
#
#
# z_1 = ComplexNumber(1, -2)
# z_2 = ComplexNumber(3, 4)
# print(z_1)
# print(z_1 + z_2)
# print(z_1 * z_2)