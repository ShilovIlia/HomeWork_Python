# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# def exponentiation(number, degree):
#     if degree != 1:
#         return number * exponentiation(number, degree - 1)
#     else: return number


# my_num = int(input("Введите число: "))
# my_degree = int(input("Введите в какую степень возвести число: "))


# print(exponentiation(my_num, my_degree))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum_two_numbers(num1, num2) -> int:
    if num2 != 0:
        return sum_two_numbers(num1+1, num2-1)
    else:
        return num1
    
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

print (sum_two_numbers(first_number,second_number))