#########################

# ДЗ 4.1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер,
# цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

# letter = 0
# count = 0
#
# text = input("enter something: ")
#
# for i in range(len(text)):
#     if text[i].isalpha() == True:
#         letter += 1
#     elif text[i].isdigit() == True:
#         count += 1
#
# print(letter)
# print(count)


# ДЗ 4.2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте
# скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.

# count = 0
#
# text = input("enter something: ")
# number = input("enter symbol to search and count: ")
#
# for i in range(len(text)):
#     if text[i] == number:
#         count += 1
#
# print(count)

# ДЗ 4.3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# text = input("enter text: ")
# word = input("enter the word you want to replace: ")
# replace = input("enter a replacement word: ")
# text = text.replace(word, replace,)
# print(text)

# ДЗ 4.4. Дано рядок. (зробити зрізи)
#
# + Спершу виведіть третій символ цього рядка.
#
# + У другому рядку виведіть передостанній символ цього рядка.
#
# + У третьому рядку виведіть перші п'ять символів цього рядка.
#
# + У четвертому рядку виведіть весь рядок, крім двох останніх символів.
#
# + У п('ятому рядку виведіть усі символи з парними індексами (вважаючи, що'
#       ' індексація починається з 0, тому символи виводяться з першого).)
#
# + У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
#
# + У сьомому рядку виведіть усі символи у зворотному порядку.
#
# + У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
#
# + У дев'ятому рядку виведіть довжину цього рядка.

# sentence = input("enter text: ")

# print(sentence[2:3])
# print(sentence[len(sentence) - 2])
# print(sentence[0:5])
# print(sentence[0:-2])
# print(sentence[1::2])
# print(sentence[::2])
# print(sentence[::-1])
# print(sentence[::-2])
# print(len(sentence))

