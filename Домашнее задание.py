# # Задача №1
# a = 7
# b = 'Привет'
# c = 777.7
#
#
# print('a =', a, '  type:', type(a))
# print('b =', b, '  type:', type(b))
# print('c =', c, '  type:', type(c))
#
# a = input('Введите a: ')
# print('a =', a, '  type:', type(a))
# b = input('Введите b: ')
# print('b =', b, '  type:', type(b))
# c = input('Введите c: ')
# print('c =', c, '  type:', type(c))
#
# print('Задание выполнено!')

# # Задача №2
#
# def convert(seconds):
#     seconds = seconds % (24 * 3600)
#
#     hour = seconds // 3600
#
#     seconds %= 3600
#
#     minutes = seconds // 60
#
#     seconds %= 60
#
#     return "%d:%02d:%02d" % (hour, minutes, seconds)
#
#
# n = 77777777
# print(convert(n))


# # Задача №3
#
# a = int(input("Введите число a: "))
# temp = str(a)
# t1 = temp + temp
# t2 = temp + temp + temp
# comp = a + int(t1) + int(t2)
# print("Результат равен:", comp)

# Задача №4

# x = 1239854
# maximum = 0
#
# while x:
#     x, n = divmod(x, 10)
#     maximum = max(maximum, n)
#
# print(f"Maximum = {maximum}")

# Задача №5

# a = int(input('Введите значение прибыли: '))
# b = int(input('Введите значение издержек: '))
#
# if a > b:
#     print('Выручка больше издержек')
#     clear_a = a - b
#
# else:
#     print('Издержки больше выручки')

# Задача №6

# a = int(input('Введите значение прибыли: '))
# b = int(input('Введите значение издержек: '))
# people = int(input('Ввдите количество работников: '))
# if a > b:
#     print('Выручка больше издержек')
#     clear_a = a - b
#     rent = clear_a/a
#     print('Рентабельность {} выручки {}: {:.2f}' .format('нашей','составила',rent))
#     clear_for_person = float(clear_a/people)
#     print('Прибыль фирмы в расчете на одного сотрудника: %s'%clear_for_person)
# else:
#     print('Фирма работает в убыток')

# Задача №7

# x = int(input('Сколько км вы пробежали сегодня?:'))
# y = int(input('Какой результат вы хотите достичь?:'))
# int(input('Сообщите нам на сколько % каждый день вы увеличиваете нагрузки и мы сообщим на какой день вы достигните результата:'))
# day = 1
# while y - x > 0:
#     x = x + (x * 0.1)
#     day += 1
#
# print(day)