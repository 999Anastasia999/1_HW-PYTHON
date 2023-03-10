# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод:   7 2 5
# Вывод:  7 9 11 13 15

a = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('ВВедите разность между ее членами: '))
n = int(input('Введите количество членов прогрессии: '))
def rec(n):
    if n == 0:
        return 0
    return (a + d*(n-1))


list = []
for i in range(1, n+1):
    list.append(rec(i))
print(*list)


# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# [-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
# 5
# 15
# Вывод: [1,9,13,14,19]

import random

n = int(input('Введите количество элементов массива: '))
list = []
for i in range(n):
    list.append(random.randint(-10, 10))
print(list)

min_num = int(input('Введите минимальный элемент диапазона: '))
max_num = int(input('Введите максимальный элемент диапазона: '))
list_new=[]
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        list_new.append(i)
print(list_new)
