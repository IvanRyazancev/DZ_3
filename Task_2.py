from random import randint
# Задача №2. Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка 
# содержит число X.

n = int(input("Введите кол-во элементов N массива A: "))
a = []
abs_n = abs(n)

for i in range(abs_n):
    a.append(randint(0, 10))
print(f"Сформированный массив:\n ", *a)

x = int(input("Введите число X (от 0 до 10), для нахождения самого близкого по величине числа: "))

if 0 <= x < 10:
    number = 0
    for i in range(len(a)):
        if a[i] == x - 1:  
            number = a[i]          
    print(f"{number} является ближайшим по величине к введенному числу {x}")
else:
    print("Введено число не входящее в массив!")