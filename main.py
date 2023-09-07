# Обробка винятків

# v1
# n1, n2 = 10, 0  # множинне привласнення
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовий тип виключення пишемо останнім з except
#     print(f"Exception occurred: {error}")
# finally:  # Відпрацьовує завжди. Писати по потребі
#     print("End of calculation")
#
# print("some text")

# У Python є такі базові типи винятків:
#
# BaseException: базовий тип для всіх вбудованих винятків
#
# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків
#
# ArithmeticError: базовий тип для винятків, пов'язаних з арифметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером
#
# LookupError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться поза допустимим діапазоном
#
# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника.
#
# OverflowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# Чисельним типом (зазвичай типом float).
#
# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії.
#
# TypeError: якщо операція або функція застосовується до значення неприпустимого типу.
#
# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням.
#
# ZeroDivisionError: виникає при розподілі на нуль.
#
# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані
#
# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import
#
# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

###
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")

#####
#
# try:
#     print("1. Start game\n2. Settings\n3. Saved games\n4. Exit")
#     user_select = int(input("Enter menu number: "))
#
#     # v1
#     if user_select == 1:
#         print("Game started")
#     elif user_select == 2:
#         print("Settings opened")
#     elif user_select == 3:
#         print("Saved games opened")
#     elif user_select == 4:
#         print("Exit...")
#     else:
#         print("Incorrect menu item!")
#
#     # v2
#     match user_select:
#         case 1:
#             print("Game started")
#         case 2:
#             print("Settings opened")
#         case 3:
#             print("Saved games opened")
#         case 4:
#             print("Exit...")
#         case _:
#             print("Incorrect menu item!")
#
# except Exception as e:
#     print(f"Error: {e}")

#############
###
# Цикли
# - while
# - for

# v1
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 1  # i = i + 1
#
#
# print("test")
#
# v2
# i = 12
#
# while True:
#     print(i)
#     i += 2

# v3
# i = 0
#
# while True:
#     if i == 5:
#         print("continue...")
#         i += 1
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i >= 10:
#         print("break...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#     i += 1
#
# print("After while")

#####################
###
# Користувач вводить з клавіатури числа
# якщо користувач ввів 0 -> припинити введення чисел
# в кінці вивести середню арифметичну числову послідовність

# sum_numbers = 0
# numbers_count = 0
#
# while True:
#     user_number = int(input("Enter number: "))
#
#     if user_number == 0:
#         print("end...")
#         break
#
#     sum_numbers += user_number
#     numbers_count += 1
#
# print(f"Sum: {sum_numbers}")
# average = sum_numbers / numbers_count
# print(f"Average: {average}")

####
# sum_num = 0
# count = 0

# try:
#     while True:
#         try:
#             num = int(input("Enter number: "))
#
#             if num == 0 and count == 0:
#                 print("Please enter a number")
#                 continue
#
#             if num == 0:
#                 print("end...")
#                 break
#
#             sum_num += num
#             count += 1
#         except ValueError as e:
#             print("Enter numbers only")
#
#     average = sum_num / count
#     print(f"sum num: {sum_num}")
#     print(f"count: {count}")
#     print(f"average: {average}")
#
# except Exception as e:
#     print

########################

# Домашнє завдання №3. 1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно
# вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок...

# try:
#     print("1. Понедельник 2. Вторник 3. Среда 4. Четверг 5. Пятница 6. Суббота 7. Воскресенье ")
#     user_select = int(input("Пожалуйста, введите номер дня недели: "))
#
#     match user_select:
#         case 1:
#             print("Понедельник")
#         case 2:
#             print("Вторник")
#         case 3:
#             print("Среда")
#         case 4:
#             print("Четверг")
#         case 5:
#             print("Пятница")
#         case 6:
#             print("Суббота")
#         case 7:
#             print("Воскресенье")
#         case _:
#             print("Некорректный номер дня недели: ")
#
# except Exception as e:
#     print(f"Error: {e}")

# Домашнє завдання №3.2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо
# ні, вивести їх на екран у порядку зростання

# try:
#     while True:
#         user_number1 = int(input("Enter first number: "))
#         user_number2 = int(input("Enter second number: "))
#
#         if user_number1 == user_number2:
#             print("Enter two different numbers:")
#         elif user_number1 < user_number2:
#             print(user_number1, user_number2)
#             break
#         elif user_number1 > user_number2:
#             print(user_number2, user_number1)
#             break
#
# except Exception as error:
#     print(f"Exception occurred: {error}")

# Домашнє завдання №3.3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

# try:
#
#     user_number1 = int(input("Enter first number: "))
#     user_number2 = int(input("Enter second number: "))
#     user_math_action = int(input("Enter the number of the desired mathematical action 1. +, 2. -, 3. *, 4. /: "))
#
#     match user_math_action:
#         case 1:
#             print(user_number1 + user_number2)
#         case 2:
#             print(user_number1 - user_number2)
#         case 3:
#             print(user_number1 * user_number2)
#         case 4:
#             print(user_number1 / user_number2)
#         case _:
#             print("Incorrect number: ")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except Exception as error:
#     print(f"Exception occurred: {error}")