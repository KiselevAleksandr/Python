# Задание №1

# my_list = []
# while True:
#     line = input("Введите данные: ")
#     if line == '':
#         print(my_list)
#         exit()
#     else:
#         newline = line + '\n'
#         my_list.append(newline)
#
#     with open("test_1.txt", "w", encoding='Utf-8') as file_obj:
#         file_obj.writelines(my_list)

# Задание №2

# my_list = ['Hello\n', 'Chao\n', 'Hola\n']
# with open("test_2.txt", 'w+') as file_obj:
#     file_obj.writelines(my_list)
# with open("test_2.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} letters in line")
#     print(f"String count is {lines}")

# Задание №3

# firm = {'Иванов': 17000, 'Петров': 21000, 'Сидоров': 19000, 'Александров': 15000}
# try:
#     file_obj = open("test_3.txt", 'w', encoding='Utf-8')
#     for last_name, salary in firm.items():
#         file_obj.write(last_name + ':' + str(salary) + "\n")
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
# summa = 0
# count = 0
# persons = []
# with open("test_3.txt", "r", encoding='Utf-8') as file_obj:
#     for line in file_obj:
#         print(line, end="")
#         tokens = line.split(':')
#         if int(tokens[1]) <= 20000:
#             persons.append(tokens[0])
#         summa += int(tokens[1])
#         count += 1
# result = summa / count
# print(f"Сотрудники: {persons}")
# print(f"Средняя: {result}")

# Задание №4

# translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
# my_list = []
# result = []
# try:
#     file_obj = open("test_4_output.txt", 'r', encoding='utf-8')
#     for line in file_obj:
#         tokens = line.split(" - ")
#         print(tokens)
#         if tokens[0] in translater:
#             word = translater[tokens[0]]
#             result.append(word +' - '+ tokens[1])
#     print(result)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
#
# try:
#     file_input = open("test_4_input.txt", "w", encoding='utf-8')
#     file_input.writelines(result)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_input.close()

# Задание №5
#
# def summary():
#     try:
#         with open('test_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел: \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

# Задание №6

# def get_num_from_str(str_with_num):
#
#
#     lst = list(str_with_num)
#     ret_val = [i for i in lst if i.isdigit()]
#
#
#     try:
#         ret_val = int(''.join(ret_val))
#     except:
#         ret_val = 0
#
#     return ret_val
#
#
# with open('test_6.txt', 'r', encoding='utf-8') as course:
#
#     course_dict = {}
#     for i in course:
#         print(i.strip())
#
#         subj = i.strip().split(': ')
#
#
#         count_str = subj[1].split(' ')
#         count_int = [get_num_from_str(j) for j in count_str]
#
#
#         subj_count = 0
#         for i in count_int:
#             subj_count += i
#
#         course_dict[subj[0]] = subj_count
#
# print('\n', course_dict)

# Задание №7

# import json
#
# with open('test_7.txt', 'r') as firm_data:
#     firm_lst = [{}, {}]
#     total_profit = 0
#     profit_count = 0
#     for i in firm_data:
#         firm_detail = i.strip().split(' ')
#         profit = int(firm_detail[2]) - int(firm_detail[3])
#         firm_lst[0][firm_detail[0] + ', ' + firm_detail[1]] = profit
#
#         if profit > 0:
#             total_profit += profit
#             profit_count += 1
#
#     firm_lst[1]['average_profit'] = total_profit / profit_count
#
# print(firm_lst)
#
# with open('test_7.json', 'w', encoding = 'UTF-8') as json_output:
#     json.dump(firm_lst, json_output, indent = 4)
