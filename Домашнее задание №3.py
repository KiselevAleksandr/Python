# Задание №1

# def my_func (a, b):
#     try:
#         c = a / b
#         return c
#     except ZeroDivisionError:
#         return "y is'n be a zero"
#     except ValueError:
#         return "enter only number"
# print(my_func(int(input("Введите число а: = ")), int(input("Введите число b: = "))))

# Задание №2

# def my_func(name, surname, byear, city, email, phone):
#     print(name, surname, byear, city, email, phone)
#
# my_func(name= 'Aleksandr', surname='Kiselev', byear=1994, city='Spb', email='email', phone='1234567')

# Задание №3

# def my_func(a, b, c):
#     sequence = [a, b, c]
#     total = []
#     max_1 = max(sequence)
#     total.append(max_1)
#     sequence.remove(max_1)
#     max_2 = max(sequence)
#     total.append(max_2)
#     print(sum(total))
# my_func(2, 17, 7)

# Задание №4

# def my_func(a, b):
#     return 1 / a ** abs(b)
#     #return x ** y
# print(my_func(3, -2))

# Задание №5

# import sys
#
# result = 0
# while True:
#     line = input("Введите числа через пробел или букву q для выхода: ")
#     tokens = line.split(" ")
#     for token in tokens:
#         try:
#             number = float(token)
#             result += number
#         except:
#             if token == 'q':
#                 print(f"Ваша сумма чисел равна: {result}. Программа завершена!")
#                 exit(0)
#             else:
#                 print(f"Ваша сумма чисела равна: {result}. Ошибка ввода!", file=sys.stderr)
#                 exit(1)
# print(result)
# exit()

# Задание №6

# def func(a):
#     return a.title()
#
# print(func("abc dfg"))

# Задание №7

# def my_func(a):
#     separate_word = a.split(' ')
#     total = []
#     for i in separate_word:
#         string_element = str(i)
#         first_letter = string_element[:1].upper()
#         word = first_letter + string_element[1:]
#         total.append(word)
#     return total
# print(my_func("Всем Привет"))