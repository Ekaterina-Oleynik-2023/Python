# Задача 10: Переворот монеток решение 1.
# n = int(input("Введите количество монет: "))
# x = 0
# for i in range(n):
#     y = int(input())
#     if y == 1:
#         x += 1
# print(x if x < n / 2 else n - x)
# ---------------------------------------------
# Задача 10: Переворот монеток решение 1.
# n = int(input("Введите количество монет: "))
# orel = 0
# reshka = 0
# for i in range(n):
#   x = int(input("Введите 0 или 1 -> "))
#   if x == 0:
#     orel += 1
#   else:
#     reshka += 1
# print(orel if reshka > orel else reshka)

# Задача 12: Отгадай числа.
# s = int(input("Сумма = "))
# p = int(input("Произведение = "))
# c = 0
# for i in range(s + p):
#     if c:
#         break
#     for j in range(s + p):
#         if i + j == s and i * j == p:
#             c = 1
#             print(("Загаданы числа ->"),i,("и"), j)

# Задача 14: целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# n = int(input("Введите число: "))
# m = 1
# while m < n:
#     print(m, end=' ')
#     m = m * 2