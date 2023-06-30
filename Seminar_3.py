# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[N].
# a = int(input("Введите количество элементов: "))
# n = list()
# for i in range(a):
#     n.append(input("Введите элементы: ")) 
# print(n)
# c = list(map(int, n))
# x = int(input("Введите число: "))
# count =0
# for i in range(a):
#     if x == c[i]:
#         count +=1
# print(f'Количество встреч числа {x} = {count}' )

# Задача 16: второй вариант.
# N = abs(int(input('Введите количество элементов списка: ')))
# ent = input("Введите через пробел элементы списка: ").split()
# num = list(map(int, ent))
# if len(num) != N:
#     print('Элементы не соответствуют заявленному количеству!')
# else:
#     x = int(input('Введите число которое необходимо найти: '))
#     count = 0
#     for i in range(N):
#         if num[i] == x:
#             count += 1
#     print(f'Количество встреч числа {x} = {count}')

#-------------------------------------------

# Задача 18: Hайти в массиве A[N] самый близкий по величине элемент к заданному числу X.

# Задача 18: не совсем правильно находит ближайший меньший элемент.
# к примеру: [1 2 3 4 5 7 9 12] X = 11 выдаст 9
# a=[int(i) for i in input("Введите через пробел элементы списка: ").split()]
# b=int(input("Введите число: "))
# number = 0
# for i in range(len(a)):
#     if (b - a[i]) < b - number and b - a[i] > 0:
#         number = i
# print(a[number])


# Задача 18: Работает вроде но не пойму как вставить ограничение по вводу...
# n = abs(int(input('Введите количество элементов: ')))
# a = input("Введите элементы списка: ").split()
# c = list(map(int, a))
# x = int(input('Введите число x: '))
# min = abs(x - c[0])
# index = 0
# for i in range(1, n):
#     count = abs(x - c[i])
#     if count < min:
#         min = count
#         index = i
# print(f'Число {c[index]} наиболее близко по величине к числу {x}')

#--------------------------------------------

# Задача 20: Scrabble.

# en = 'abcdefghijklmnopqrstuvwxyz'
# ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#       4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# Rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#       4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
# word = input('Введите слово: ')
# if word[0].lower() in en:
#     sum = 0
#     for letter in word:
#         for key, value in Eng.items():
#             if letter.upper() in value:
#                 sum += key
#     print(("Стоимость слова"), "=", (sum))
# else:
#     if word[0].lower() in ru:
#         sum = 0
#         for letter in word:
#             for key, value in Rus.items():
#                 if letter.upper() in value:
#                     sum += key
#     print(("Стоимость слова"), "=", (sum))

# Задача 20. Scrabble. Решение с функцией.

# import re
# def isCyrillic(text):
#   return bool(re.search('[а-яА-Я]', text))
# en = {1:'AEIOULNSTR',2:'DG',3:'BCMP',
#             4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
# ru = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',
#             4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
# text = input("Введите слово: ").upper()
# if isCyrillic(text):
#   print(sum([k for i in text for k, v in ru.items() if i in v]))
# else:
#   print(sum([k for i in text for k, v in en.items() if i in v]))