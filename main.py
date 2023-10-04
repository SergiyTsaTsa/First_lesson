#######################
# ДЗ 9.1  Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу
# всі слова, що складаються не менше ніж з семи літер.

# with open("lesson11_original.txt", "w") as lesson11_original:
#     lesson11_original.write('To be, or not to be, that is the question, Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart - ache and the thousand natural shocks That flesh is heir to, tis a consummation Devoutly to be wishd. To die, to sleep')
# with open("lesson11_original.txt", "r") as lesson11_original:
#     for line in lesson11_original:
#         words = line.split()
# long_words = [word for word in words if len(word) >= 7]
# with open("lesson11_new.txt", "w") as lesson11_new:
#     lesson11_new.write(" ".join(long_words) + "\n")

# ДЗ 9.2. Даний текстовий файл. Підрахувати кількість слів у ньому.

# with open("lesson11_original.txt", "w") as lesson11_original:
#     lesson11_original.write('To be, or not to be, that is the question, Whether tis nobler in the mind to suffer '
#                             'The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart - ache and the thousand natural shocks That flesh is heir to, tis a consummation Devoutly to be wishd. To die, to sleep')
# with open("lesson11_original.txt", "r") as lesson11_original:
#     new_command = lesson11_original.read() # Нашел такую функцию в описалке работы с файлами в python.
#     # Вроде на уроке о ней не было сказано. используется для чтения содержимого файла после открытия его в режиме чтения.
#     words = new_command.split()
#     word_count = len(words)
# print("Number of words in file:", word_count)