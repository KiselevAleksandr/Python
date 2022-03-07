# Задание №1
#
# my_int = 5
# my_float = 1.2
# my_str = "Всем привет"
# my_list = ['a', '2']
# my_tuple = ('b', '3')
# my_dict = {'Город': 'Санкт-Петербург', 'Страна': 'Россия'}
#
# super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
# for i in super_list:
#     print(f'{i} is {type(i)}')

# Задание №2
#
# my_list = ['1', '2', '3', '4', '5']
# if len(my_list) % 2 == 0:
#     i = 0
#     while i < len(my_list):
#         el = my_list[i]
#         my_list[i] = my_list[i+1]
#         my_list[i+1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(my_list) - 1:
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i += 2
# print(my_list)

# Задание №3

# number = int(input("Введите номер месяца: "))
# if number <= 12 and number >= 1:
#     month_dict = {1: 'Зима',
#                   2: 'Зима',
#                   3: 'Весна',
#                   4: 'Весна',
#                   5: 'Весна',
#                   6: 'Лето',
#                   7: 'Лето',
#                   8: 'Лето',
#                   9: 'Осень',
#                   10: 'Осень',
#                   11: 'Осень',
#                   12: 'Зима'}
#     month_list = list(month_dict.values())
#     for i, el in enumerate(month_list):
#         if i == number-1:
#             print(f"Month from list is {month_list[i]}")
#             break
#     print(f"Month from dict is {month_dict[number]}")
# else:
#   print("You made a mistake")

# Задание №4

# my_str = input("Введите предложение: ")
# a = my_str.split(' ')
# for i, el in enumerate(a, 1):
#     if len(el) > 10:
#         el = el[0:10]
#     print(f"{i}. - {el}")

# Задание №5
#
# number = int(input("Ведите число: "))
# my_list = [7, 6, 5, 4]
# c = my_list.count(number)
# for element in my_list:
#     if c > 0:
#         i = my_list.index(number)
#         my_list.insert(i+c, number)
#         break
#     else:
#         if number > element:
#             j = my_list.index(element)
#             my_list.insert(j, number)
#             break
#         elif number < my_list[len(my_list) - 1]:
#             my_list.append(number)
# print(my_list)

# Задание №6

# goods = []
# number = 0
#
# print('Введите одной строкой название товара, цену, количество и единицу измерения')
# print('В качестве разделителя позиций используйте только один символ запятой')
# print('Значения цены и количества должны быть целочисленными')
# print('Для завершения введите пустую строку')
#
# while True:
#     number += 1
#     good_list = input(f'{number} товар: ').split(',')
#     if good_list == ['']:
#         break
#
#
#     goods.append((number, {'Наименование': good_list[0],
#                            'Цена': int(good_list[1]),
#                            'Количество': int(good_list[2]),
#                            'Ед. изм.': good_list[3]}))
#
#
# goods_dict = {}
#
# for i, el in enumerate(list(goods[0][1].keys())):
#
#     goods_dict[el] = []
#
# for i, el in enumerate(goods_dict):
#
#     dict_list = []
#
#
#     for j, el_goods in enumerate(goods):
#         key_val = el_goods[1].get(el)
#
#
#         if key_val not in dict_list:
#             dict_list.append(key_val)
#
#
#     goods_dict[el] = dict_list
#
# print(goods_dict)

