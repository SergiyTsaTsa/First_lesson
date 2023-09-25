#######################
# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.

# def my_pow(number, degree):
#     if degree <= 1:
#         return number
#
#     return number * my_pow(number, degree - 1)
#
# print(my_pow(2, 3))
#
# # my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# # my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# # my_pow(2, 1) => 2

# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

# number = int(input("enter the number of stars: "))
# i = "*"
# def stars(number):
#     if number <= 1:
#         return i
#     print(i, end=" ")
#     return stars(number-1)
#
# print(stars(number))

# для примера, number = 5:
# 5 -> *  возврат 5-1=4 ->
# 4 -> *  возврат 4-1=3 ->
# 3 -> *  возврат 3-1=2 ->
# 2 -> *  возврат 2-1=1 ->
# 1 -> срабатывает первое условие number <= 1: и возвращается *, последняя из заданных
# так как print(i, end=" ") с пробелом, то все звездочки красиво в одну строчку с пробелом)



# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# def sum(a, b):
#     if a > b:
#         return 0
#
#     return a + sum(a+1, b)
#
# print(sum(a, b))

# для примера, a = 1, b = 5:
# 1  + (1+1) -> 3  возврат a = 2, sum = 3  ->
# 3  + (2+1) -> 6  возврат a = 3, sum = 6  ->
# 6  + (3+1) -> 10 возврат a = 4, sum = 10 ->
# 10 + (4+1) -> 15 возврат a = 5, sum = 15 ->
# срабатывает первое условие if а=5+1 > b=5, цикл закакнчивает работу


# Завдання 4. Додаткове
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином
# і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.

# Попытка решить дополнительно задание. с рекурсией не вышло. без рекурсии работает

# import random
#
# mylist = [random.randint(1, 10) for i in range(100)]
# print(mylist)
#
#
# def find_minindex_for_tenitems(list):
#     minsum = 0
#     index = 0
#     for i in range(len(list)):
#         sum = 0
#         if (i + 10 > len(list)):
#             print("minsum: " + str(minsum))
#             return index
#
#         for j in range(i, i + 10):
#             sum += list[j]
#
#         if (i == 0):
#             minsum = sum
#         if (minsum > sum):
#             minsum = sum
#             index = i
#
#             print(sum, end = " ")
#
#
# print("Index: " + str(find_minindex_for_tenitems(mylist)))
##############################################################