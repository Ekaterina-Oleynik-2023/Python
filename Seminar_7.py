# Задача 34: Винни пух.

# poetry = input("Введите стих: ").lower().split() 
# vowel = [sum(x in "уеыаоэяию" for x in lin) for lin in poetry]
# if len(set(vowel)) == 1 :
#     print("--- Парам пам-пам ---")
# else: print("--- Пам парам ---")


# ---------------------------------------------------------------


#  Задача 36: Напишите функцию, которая принимает в качестве аргумента функцию, 
#  вычисляющую элемент по номеру строки и столбца.

# -------решение покрасивее--------
# def print_operation_table(operation, num_rows, num_columns):
#     list = [[operation(i, j) for j in range(1 , num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in list:
#          print(*[f"{x:>2}" for x in i])
# print_operation_table(lambda x, y: x * y, int(input("Строк: ")), int(input("Столбцов: ")))

# -------решение проще--------
# def print_operation_table(operation, num_rows, num_columns):
#     for i in range(1 , num_rows + 1):
#         list = []
#         for j in range(1, num_columns + 1):
#             list.append(i * j)
#         print(*list)  
# print_operation_table(lambda x, y: x * y, int(input("Строк: ")), int(input("Столбцов: ")))