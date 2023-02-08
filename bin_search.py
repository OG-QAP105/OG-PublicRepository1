# Функция сортировки (метод пузырька) списка по возрастанию элементов в нем:
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

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
        return middle+1
    else:
        return middle

# На вход подается последовательность чисел через пробел, преобразование введённой последовательности в список,
# а также запрашивается у пользователя любое число.
my_list = list(map(int, input("Введите массив чисел через пробел: ").split()))

# Определяем граничные индексы:
my_low = 0
my_high = len(my_list)-1

# Сортировка списка:
my_list = bubble_sort(my_list)
print(my_list)

my_number = int(input("Введите любое число в интервале от " + str(my_list[0]) + " до "
                      + str(my_list[len(my_list)-1]) + " : "))

if my_low <= my_number <= my_high:
    print("Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу, "
          "равен:", binary_search(my_list, my_number, my_low, my_high))
else:
    print("Введенное число не попадает в границы массива!")








