# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141


# import math
# from math import pi

# n = pi
# print(n)

# n = 1
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(my_pi)




# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input('Введите число N: '))
# list = []
# a = n
# if n > 1:
#     restart = True
#     while restart:
#         restart = False
#         for i in range (2, n+1):
#             if n%i == 0:
#                 list.append(i)
#                 n = int(n/i)
#                 restart = True
#                 break

#     print(f'Простые множители числа {a} - {list}')
# elif n == 1:
#     print(f'Простые множители числа {a} - [1]')
# else:
#     print(f'Вы ввели не правильное число')





# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


# A = [1, 1, 2, 3, 4, 4, 4]
# found = set()
# found_again = set()

# for a in A:
#     if a in found_again:
#         continue
#     if a in found:
#         found.remove(a)
#         found_again.add(a)
#     else:
#         found.add(a)

# print(list(found))



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.


# from random import randint
# max_val=100
# k = int(input('Введите натуральную степень k:'))
# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly+=('','1')[poly[-1]=='+']
# poly=(poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)










