# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# number_of_elements = int(input("Введите количество элементов списка: "))
# step_between_elements = int(input("Введите шаг между элементами: "))
# first_element = int(input("Введите первый элемент списка: "))

# my_list = [i for i in range(first_element, (first_element + (number_of_elements-1)*step_between_elements) +1, step_between_elements)]

# print(*my_list, sep='\n')


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# number_of_elements = int(input("Введите количество элементов списка: "))

# min_value = int(input("Введите минимальную границу поиска индексов элементовсписка: "))
# max_value = int(input("Введите максимальную границу поиска индексов элементовсписка: "))

# my_list = [random.randint(0,10) for _ in range(number_of_elements)]

# def search_index_element(my_list: list, min: int, max: int):
#     rez_list = []
#     for i in range (len(my_list)):
#         if min <= my_list[i] <= max:
#             rez_list.append(i)
#     return rez_list

# print(my_list)
# print(search_index_element(my_list, min_value, max_value))