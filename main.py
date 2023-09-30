#######################
# ДЗ 10 Написати валідації за допомогою регулярних виразів:
#
# ДЗ 10.1 домашній номер телефону (тільки цифри та довжина номера)

# import re
#
# li = ['0482-37-35-40', '048-730-25-96', '+38-066-295-18-25', '+38-050-499-38-24', '09928796482147', '0482-44-29-16',
#       '048-499-22-19', 'hello world', '0482-33-18-85', '+38-099-25-65', '+38-067-17-22']
#
# for val in li:
#     if re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}', val) and len(val) == 13:
#         print(val)
#     elif re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}', val) and len(val) == 13:
#         print(val)
#     else:
#         print('incorrect number')

# 10.2 Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# import re
#
# li = ['0482-37-35-40', '048-730-25-96', '+38-066-295-18-25', '+38-050-499-38-24', '0992879648', '0482-44-29-16',
#       '048-499-22-19', 'hello world', '0482-33-18-85', '38-099-422-25-65', '38-067-222-17-22']
#
# for val in li:
#     if re.findall(r'[+]?[0-9]{2}-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', val) and 10 <= len(val) <= 17:
#         print(val)
#     elif re.findall(r'[0]{1}[0-9]{9}', val) and len(val) == 10:
#         print(val)
#     else:
#         print('incorrect number')

# 10.3 email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

# import re
#
# li = ['test@gmail.com', '+38-050-499-38-24', '0992879648', 'lesson10@gmail.com', '0482-44-29-16',
#       'hello world', '0482-33-18-85', 'Serega_znaet@gmail.com', '38-099-422-25-65', '38-067-222-17-22']
#
# for val in li:
#     if re.findall(r'\w+@\w+.\w+', val) and 12 <= len(val) <= 30:
#         print(val)
#     else:
#         print('incorrect email')

# 10.4 ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# import re
#
# li = ['Zagoruyko Petro Fedorovich', '+38-050-499-38-24', '0992879648', 'lesson10@gmail.com', 'Ivanov Moysha Isaakovich',
#       'hello world', '0482-33-18-85', 'Serega_znaet@gmail.com', 'Umapalata Nauseda Proebaltovna', '38-067-222-17-22']
#
# for val in li:
#     if re.findall(r'\w+[ ]\w+[ ]\w+', val) and 6 <= len(val) <= 60:
#         print(val)
#     else:
#         print('incorrect name')
