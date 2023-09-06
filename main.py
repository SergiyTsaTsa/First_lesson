
# number1 = int(input("введите цифру 1: "))
# numder2 = int(input("введите цифру 2: "))
# number3 = int(input("введите цифру 3: "))
#
# print(number1 + numder2 + number3)
# print(number1 * numder2 * number3)
#
# side1 = int(input("введите длину диагонали 1: "))
# side2 = int(input("введите длину диагонали 2: "))
#
# print(int((side1*side2)/2))
#
# number = int(input("введите четырехзначное число: "))
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number // 10 % 10
# n4 = number % 10
# print(n1 * n2 * n3 * n4)

###################
# умови
# v1
# n1 = 10 + 20 * 2  # оператор привласнення, отрабатывает последним
# n2 = 20
# v2
# n1, n2 = 10, 20 + 10  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
#
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
#
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки

# print("hello" in "hello world")
# hours = int(input("enter hours: "))

# v1
# if hours >= 12:
#     print("PM")
# else:
#     print("AM")

# if 12 <= hours < 24:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("ncorrect hours!")
#
# print("Hello world")

# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK")
#     else:
#        print("Not ok")
# else:
#     print("Incorrect rating")
