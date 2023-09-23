#######################
# Завдання 1
#
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# результат повертається із функції.
# import random
#
# numbers = []
#
# for _ in range(10):
#     numbers.append(random.randint(1, 10))
#
# print(numbers)
# def get_list_multiplication(numbers):
#     numbers_multiplication = 1
#
#     for num in numbers:
#         numbers_multiplication *= num
#
#     return numbers_multiplication
#
# my_numbers = numbers
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
#
# result = minList(numbers)
# print(result)

# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# import random
# numbers = []
#
# for _ in range(10):
#     numbers.append(random.randint(1, 10))
# print(numbers)
# def sumList(numbers):
#     count = 0
#     for number in numbers:
#         is_simple = True
#
#         if number < 2:
#             continue
#         for i in range(2, number):
#             if number % i == 0:
#                 is_simple = False
#                 break
#         if is_simple:
#             count += 1
#     return count
#
# result = sumList(numbers)
# print(result)

# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів
# import random
# def create_list_with_random_values(list_length=10, start_value=1, end_value=10) -> list:
#     new_list = []
#     for _ in range(list_length):
#         new_list.append(random.randint(start_value, end_value))
#     return new_list
#
# my_numbers = create_list_with_random_values()
# print(my_numbers)
#
# number = int(input("enter a number from the list: "))
# def delete_items(my_numbers, number):
#     count = 0
#     Copy_list = my_numbers.copy()
#     for i in my_numbers:
#         if i == number:
#             Copy_list.remove(number)
#             count += 1
#     print(Copy_list)
#     return count
# print(delete_items(my_numbers, number))

# Завдання 5
#
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків

# import random
#
# def create_list_with_random_values_1(list_length=10, start_value=1, end_value=10) -> list:
#     new_list_1 = []
#
#     for _ in range(list_length):
#         new_list_1.append(random.randint(start_value, end_value))
#     return new_list_1
#
# my_numbers_1 = create_list_with_random_values_1()
# print(my_numbers_1)
#
# def create_list_with_random_values_2(list_length=10, start_value=1, end_value=10) -> list:
#  new_list_2 = []
#
#  for _ in range(list_length):
#   new_list_2.append(random.randint(start_value, end_value))
#  return new_list_2
#
# my_numbers_2 = create_list_with_random_values_2()
# print(my_numbers_2)
#
# def list_gen(my_numbers_1, my_numbers_2):
#     combined_list = [my_numbers_1, my_numbers_2]
#     new_list = [i for sublist in combined_list for i in sublist]
#     return new_list
#
# print(list_gen(my_numbers_1, my_numbers_2))

# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
# список також передається як параметр. Функція повертає новий список, який містить отримані результати.

# import random
# def create_list_with_random_values(list_length=10, start_value=1, end_value=10) -> list:
#     new_list = []
#
#     for _ in range(list_length):
#         new_list.append(random.randint(start_value, end_value))
#     return new_list
#
# my_numbers = create_list_with_random_values()
# print(my_numbers)
#
# degree = int(input("enter the power of the number: "))
# def my_pow(my_numbers, degree):
#     new_list_1 = []
#     if degree <= 1:
#         return my_numbers
#
#     for i in my_numbers:
#         new_list_1.append(i ** degree)
#     return new_list_1
#
# print(my_pow(my_numbers, degree))