"""
Задание 22.8.1
Найдите количество цифр в записи числа 100! (факториал от 100).
"""

n = int(input("Введите целое число: "))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(len(str(factorial)))
