#######################
# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# + Суму негативних чисел;
#
# + Суму парних чисел;
#
# + Суму непарних чисел;
#
# + Добуток елементів з кратними індексами 3;
#
# + Добуток елементів між мінімальним та максимальним елементом;

# + Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# Lesson 5.1.1
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-10, 10))
#
#     while i >= 0 and numbers[i] < 0:
#         total += numbers[i]
#         break
#
# print(numbers)
# print (total)

# Lesson 5.1.2
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
#     while numbers[i] % 2 == 0:
#         total += numbers[i]
#         break
#
# print(numbers)
# print (total)

# Lesson 5.1.3
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# sum_numbers = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#     while numbers[i] % 2 != 0:
#         sum_numbers += numbers[i]
#         break
#
# print(numbers)
# print (sum_numbers)

# Lesson 5.1.4
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# sum_numbers = 1
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#     while (i + 1) % 3 == 0:
#         sum_numbers = numbers[i] * sum_numbers
#         break
#
# print(numbers)
# print (sum_numbers)

# Lesson 5.1.5
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# sum_numbers = 1
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
# min_value = min(numbers)
# max_value = max(numbers)
#
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# print(min_value_index)
# print(max_value_index)
#
# if min_value_index > max_value_index:
#     min_value_index, max_value_index = max_value_index, min_value_index
#
# for i in range(min_value_index + 1, max_value_index):
#     sum_numbers *= numbers[i]
#
# print(numbers)
# print (sum_numbers)
# print(min_value)
# print(max_value)

# Lesson 5.1.6
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# number1 = 0
# number2 = 0
# sum_numbers = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-10, 10))
#
# for number1, a in enumerate(numbers): # обращается одновременно к индексу и к значению єлемента коллекции, разобрался, так как был большой затык в вывполнении этого подзадания
#     if a > 0:
#         break
# for number2, a in enumerate(reversed(numbers)): # про reversed вы упоминали на занятии, при разборе домашки, поэтому пришлось разобраться)
#     if a > 0:
#         break
# sum_numbers = sum(numbers[number1 + 1: -number2 - 1]) # такая конструкция вроде и не озвучивалась, но sum и отрицательный number2 получен путем множества проб и ошибок
#
# print(numbers)
# print (sum_numbers)

# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# + Створити список цілих, що містить лише парні числа з першого списку;
#
# + Створити список цілих, що містить лише непарні числа з першого списку;
#
# + Створити список цілих, що містить лише негативні числа з першого списку;

# + Створити список цілих, що містить лише позитивні числа з першого списку.

# Lesson 5.2.1
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
#     while numbers[i] % 2 == 0:
#         print(numbers[i], end=" ")
#         break
#
# print(numbers)

# Lesson 5.2.2
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
#     while numbers[i] % 2 != 0:
#         print(numbers[i], end=" ")
#         break
#
# print(numbers)

# Lesson 5.2.3
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-10, 10))
#
#     while numbers[i] < 0:
#         print(numbers[i], end=" ")
#         break
#
# print(numbers)

# Lesson 5.2.4
# import random
#
# NUMS_SIZE = 10
# numbers: list[int] = []
# i = len(numbers)
# total = 0
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-10, 10))
#
#     while numbers[i] > 0:
#         print(numbers[i], end=" ")
#         break
#
# print(numbers)