#######################
# Завдання 1
#
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# результат повертається із функції.

# def get_list_multiplication(numbers):
#     numbers_multiplication = 1
#
#     for num in numbers:
#         numbers_multiplication *= num
#
#     return numbers_multiplication
#
#
# my_numbers = [n for n in range(1, 10)]
# print(my_numbers)
# result = get_list_multiplication(my_numbers)
# print(result)

# Завдання 2
#
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# import random
#
# numbers = []
#
# for _ in range(10):
#     numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# def minList(numbers):
#     if len(numbers) > 0:
#        min = numbers[0]
#     for i in range(1,len(numbers)):
#        if numbers[i] < min:
#            min = numbers[i]
#     return min
# print(minList(numbers))

# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

import random
numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 10))

print(numbers)
def simple(numbers):
    count = 0
    for i in range(numbers):
        if numbers % i == 0:
            count = count + 1
        return count
    print(count)

# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно
# повернути кількість видаленних елементів.

