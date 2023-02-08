"""
Допустим, намотали на ус, что перестановками нам ничего хорошего не добиться.
Следующее решение «в лоб» — каждый раз искать минимальный элемент и ставить его в начало. Звучит уже интереснее.
"""

# Задание 22.8.2
# Посчитайте количество сравнений, которые производятся в алгоритме выбором из примера.

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
        count += 1
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]


print(array)

print(count)


# Задание 22.8.3
# Модифицируйте описанный алгоритм для сортировки по убыванию.
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
        count += 1
    if i != idx_max:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_max] = array[idx_max], array[i]


print(array)

print(count)
