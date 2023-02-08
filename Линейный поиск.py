"""
Пусть на вход программы поступает массив из произвольного количества целых чисел и ещё одно целое число,
которое будем проверять на вхождение в этот массив. Задача состоит в том, чтобы вернуть индекс
первого вхождения элемента, если он входит в него, и False если не входит.
"""

def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input("Введите массив чисел:").split()))
print(array)
element = int(input("Введите число:"))
print(element)

print(find(array, element))

