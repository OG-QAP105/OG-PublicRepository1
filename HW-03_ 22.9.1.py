# Функция сортировки (метод пузырька) списка по возрастанию элементов в нем:
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Функция проверки ввода целого положительного числа:
def digit_check(list, low, high):
    try:
        input_number = int(input(f'\n>> Введите число, которое  > {list[low]} и <= {list[high]} : '))
        if not (list[low] < input_number <= list[high]):
            raise ValueError
    except ValueError:
        print("\033[31m<< Введенное число не попадает в границы массива! >>\033[37m")
        input_number = digit_check(list, low, high)
    return input_number

# Функция двоичного поиска:
def binary_search(list, number, low, high):

    middle = len(list) // 2
    while list[middle] != number and low <= high:
        if number > list[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (low + high) // 2

    if low > high:
        return middle
    else:
        return middle-1

# На вход подается последовательность чисел через пробел, преобразование введённой последовательности в список,
# а также запрашивается у пользователя любое число.
my_list = list(map(int, input("\n>> Введите массив чисел через пробел  : ").split()))

# Определяем граничные индексы:
my_low = 0
my_high = len(my_list)-1

# Сортировка списка:
my_list = bubble_sort(my_list)
print("\nОтсортированный список введенных чисел:", my_list)

my_number = digit_check(my_list, my_low, my_high)

print("\n\033[32mИскомый номер позиции элемента равен  :\033[37m", binary_search(my_list, my_number, my_low, my_high))



