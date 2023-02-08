"""
Задание 22.7.1
Напишите функцию count, которая возвращает количество вхождений элемента в массив
"""

def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count

array = list(map(int, input("Введите массив чисел: ").split()))

element = int(input("Введите число: "))

print(count(array, element))
