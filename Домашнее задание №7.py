# Задание №1

# class Matrix:
#     def __init__(self, list_1, list_2):
#         self.list_1 = list_1
#         self.list_2 = list_2
#
#     def __add__(self):
#         matr = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]
#
#         for i in range(len(self.list_1)):
#
#             for j in range(len(self.list_2[i])):
#                 matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
#
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
#
#
# my_matrix = Matrix([[1, 14, 12],
#                     [5, 12, 35],
#                     [34, 50, 11]],
#                    [[5, 12, 3],
#                     [15, 7, 32],
#                     [26, 11, 76]])
#
#
# print(my_matrix.__add__())

# Задание №2

# class Textil:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def get_sq_full(self):
#         return str(f'Общая площадь ткани \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
#
# class Coat(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = round(self.width / 6.5 + 0.5)
#
#     def __str__(self):
#         return f'Площадь на пальто {self.square_c}'
#
#
# class Jacket(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = round(self.height * 2 + 0.3)
#
#     def __str__(self):
#         return f'Площадь на костюм {self.square_j}'
#
# coat = Coat(2, 4)
# jacket = Jacket(1, 2)
# print(coat)
# print(jacket)
# print(coat.get_sq_full)
# print(jacket.get_sq_full)
# print(jacket.get_square_c())
# print(jacket.get_square_j())

# Задание №3


# class cell():
#
#     def __init__(self, cell_count):
#         self.cell_count = cell_count
#
#     def __add__(self, other):
#         return self.cell_count + other.cell_count
#
#     def __sub__(self, other):
#         ret_val = self.cell_count - other.cell_count
#         return  ret_val if ret_val > 0 else 'error'
#
#     def __mul__(self, other):
#         return self.cell_count * other.cell_count
#
#     def __truediv__(self, other):
#         return self.cell_count // other.cell_count
#
#     def make_order(self, row_cells):
#         self.row_cells = row_cells
#
#         return ('*' * self.row_cells + '\n') * (self.cell_count //self.row_cells) + '*' * (self.cell_count % self.row_cells)
#
#
# c1 = cell(25)
# c2 = cell(5)
#
# print(c1 + c2)
# print(c1 - c2)
# print(c1 * c2)
# print(c1 / c2)
#
# print(c1.make_order(15))
