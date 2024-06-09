# def print_messages():
#     print("Hello1")
#     print("Hello2")
#     print("Hello3")
#     print("Hello4")
#
# print()
# print_messages()
# print_messages()
# print_messages()
# print_messages()

# def my_function(params):
# ....code..

# call function :
# my_function(args)


# name = "Den"
# age = 20
#
#
# def foo(name, age):  # параметри
#     print("Hello " + name, " your age " + str(age))
#
#
# foo("John", 20)  # аргумент
# foo("Nick", 30)
# foo(name, 50)


# def foo_math(n1, n2): # return
#     print("Start ")
#
#     return n1 + n2  #
#     print("End ")
#
# y = 101
# res = foo_math(5, 2)
#
# x = y + res
# print(x)

# users = {'admins': ['John', 'Den'], 'users': ['alex', 'Micky'], 'moderators': ['Nick']}
#
#
# def wellcome_message(name: str) -> None:
#     for key, item in users.items():
#         if name in item:
#             if 'admin' in key:
#                 print("Вітаю адмін! " + name.capitalize())
#             elif 'user' in key:
#                 print("Вітаю користувач! " + name.capitalize())
#             elif 'moder' in key:
#                 print("Вітаю модератор! " + name.capitalize())
#
# print(wellcome_message('alex'))

# def foo(x, y: int | str) -> int | str | None:
#     if x == 1:
#         return y + x
#     elif x == "1":
#         return y - x
#     else:
#         return
#
#
# x = foo(5,8)
# def foo_inner(x,y):
#     print(x,y)
#
# def foo(*args, **kwargs):
#     foo_inner(**kwargs)
#     print(args)
#
#
# foo(5, 4, 3, 2, 1, y=10, x=20)

# def foo(number1, number2, number3, x=0, y=0):
#     print(number1, number2, number3, x, y)
#
#
# foo(1, 2, 3, 4, 5)
# foo(1, 2, 3)
# foo(1, 2, 3)
# foo(1, 2, 3, 4, 5)
#
# foo(1, 2, 3,5, 2)

# import random
#
# print(random.randint(1,2))

# from random import randint
#
# print(randint(1,2))

# from random import randint as ri, random as r
#
# print(ri(1,2))

# import funcs
# import datetime
#
# funcs.prefix_message("Hello", "Alex: ")
#
# now = datetime.datetime.now()
# print(now.month)
# formatted_date = now.strftime(funcs.DATETIME_FORMAT)
# print(formatted_date)
# x = input("Enter number")
# if isinstance(x, int):
#     print(x+5)

# Напишіть функцію, яка перевіряє чи є шестизначне
# число «щасливим». Число передається як параметр. Якщо
# число щасливе, поверніть з функції true, якщо ні — false.
# «Щасливе шестизначне число» — це число, в якому
# сума перших трьох цифр дорівнює сумі других трьох
# цифр. Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а
# 723422 — нещасливе 7+2+3 != 4+2+2.

# def is_lucky_number(number):
#     if not isinstance(number, int) or not 100000 <= number <= 999999:
#         return False
#
#     n_str = str(number)
#     # 123321
#     # * args , sum(1,2,3)
#     sum_first_three = sum(int(n_str[i]) for i in range(3))
#     sum_last_three = sum(int(n_str[i]) for i in range(3, 6))
#
#     return sum_first_three == sum_last_three
#
#
# print(is_lucky_number(123321))
# print(is_lucky_number(123456))
# print(is_lucky_number(1))
# print(is_lucky_number("123"))


# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат із певним символом.
# Функція приймає в якості
# параметрів довжину сторони квадрата, символ та змінну
# логічного типу:
# ■ якщо вона дорівнює True, квадрат заповнений;
# ■ якщо False, квадрат порожній.

# def draw_square(side, symb, filled):
#     symb += " "
#     if filled:
#         for _ in range(side):
#             print(symb * side)
#     else:
#         print(symb * side)
#         for _ in range(side - 2):
#             print(symb + "  " * (side - 2) + symb)  # *   *
#         print(symb * side)
#
#
# draw_square(5, '*', True)
# print()
# draw_square(5, '*', False)

# def foo(x):
#
#     x += 2
#     return x
#
#
# res = foo(0)
# y = res
# x = 5
# b = None
# if x == 5:
#     b = 7
#
# def foo():
#     global x
#     global b
#     if b is not None:
#         print(b)
#     print(b)
#     x += 10
#
#
# print(x)
# foo()
# print(x)


# def foo(n):
#     if n == 0:
#         return 1
#     else:
#         return n * foo(n - 1)
#
# n1 = 5
# n2 = 10
# print(foo(n1,n2)) # 120

# n = 5
# res = 1
# for i in range(1, n+1):
#     print(i, end=' ')
#     res *=i
# print(res)
# inner call
# if cond: return

# Створіть гру «Хрестики-Нулики».

# board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#
# def print_board():
#     for i, row in enumerate(board):
#         print(" | ".join(row))
#         if i != 2:
#             for i in range(9):
#                 if i == 2 or i == 6:
#                     print("+", end="")
#                 else:
#                     print("-", end="")
#             print()
#
#
# def make_move(cell, current_player):
#     row, col = cell // 3, cell % 3
#     if board[row][col] == str(cell + 1):
#         board[row][col] = current_player
#         return True
#     return False
#
#
# def check_winner(current_player):
#     for i in range(3):
#         if board[i][0] == current_player and board[i][1] == current_player and board[i][2] == current_player:
#             return True
#
#     for i in range(3):
#         if board[0][i] == current_player and board[1][i] == current_player and board[2][i] == current_player:
#             return True
#
#     if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
#         return True
#
#     if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
#         return True
#
#
# def main():
#
#     current_player = 'X'
#     moves_count = 0
#     while True:
#         print_board()
#         cell = int(input(f"Player {current_player}, enter numb cell: ")) - 1
#         if 0 <= cell <= 8 and make_move(cell, current_player):
#             if check_winner(current_player):
#                 print_board()
#                 print(f"Player {current_player} Winner!")
#                 break
#             moves_count += 1
#             if moves_count == 9:
#                 print("Draw!")
#                 break
#
#             current_player = 'O' if current_player == 'X' else 'X'
#             # if current_player == 'X':
#             #     current_player = 'O'
#             # else:
#             #     current_player='X'
#         else:
#             print("Incorrect range or cell busy..")
#
#
# if __name__ == '__main__':
#     main()


# Створити функцію, яка приймає два аргументи це діапазони (start, stop)
# та визначає рекурсивним методом сумму чисел в діапазоні,
# користувач вводить діапазон наприклад 2 і 5 результат має бути 14


# lambda params: expression

# d = lambda x: x * 2
# print(d(5))

# def foo(x, action):
#     return action(x) + 5
#
# print(foo(5, lambda y: y*2))
# print(foo(5, lambda y: y*5))
# print(foo(5, lambda y: y*2))

# students = [['Bob', 70],
#             ['Jane', 80],
#             ['Andy', 50]
#             ]
# print(students)
# sortedSts = sorted(students, key=lambda x: x[1])
# print(sortedSts)

# map
# def foo(x):
#     y =x*2
#     #
#     #
#     return y
# ls = [1, 2, 3, 4, 5]
# print(list(i*2 for i in ls))
# print(list(map(foo, ls)))
# reduce
# from functools import reduce
#
# ls2 = []
#
#
# def foo(x, y):
#     res = x + y
#     ls2.append(res)
#     return res
#
#
# ls = [1, 2, 3, 4, 5]
# # 1 2 3 4 5
# # 1+2 3
# # 3+3 6
# # 6+4 10
# # 10+5 15
# print(reduce(foo, ls))
# print(ls2)

# prices = [100.45, 8.56, 5, 234, 45, 87, 567]
# expensive = filter(lambda x: x >= 10, prices)
# print(expensive)  # [100.45, 234, 45, 87, 567]

# userLogs = ['123user45', 'USERstudent', '56use3', 'user-23',
#             'adminUs']
#
#
# def checkLog(user: str):
#     if user.lower().find('user') != -1:
#         return True
#     else:
#         return False
#
#
# selectedUser = list(filter(checkLog, userLogs))
# print(selectedUser)
# zip

# students = ['alex', 'den']
# math_grades = [55, 66]
# physics_grades = [22, 99]
# for s, m, p in zip(students, math_grades, physics_grades):
#     print(f"{s}: math = {m}, physics = {p}, avg = {((m + p) / 2):.2f}")


# from functools import partial, cmp_to_key, lru_cache


# reduce, partial,  cmp_to_key

# lru_cache

# partial
# def mult(*args):
#     ls = list(args)
#
#     return
#
#
# p = partial(mult, 5,2,1)
# print(p(7))
# print(p(2))
# print(p(1))

# cmp_to_key

# def comp_items(x, y):
#     return x - y
#
#
# ls = [1, 5, 3, 4, 2, -10]
#
# s_ls = sorted(ls, key=cmp_to_key(comp_items))
# print(s_ls)
# def sayUserHello(user):
#     msg = "Hello, " + user
#
#     def showMsf():
#         print(msg + "! Let's start...")
#
#     showMsf()
#
# sayUserHello('admin')


# def make_mult(x):
#     y = 10
#
#     def mult(n):
#         return x * n - y
#
#     return mult
#
#
# x = make_mult(5)
#
# print(x(10))

# def foo(x,y):
#     return x+y
#
# print(foo(5,5))
# print(foo(15,6))
# print(foo(17,10))

# def make_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
#
# counter = make_counter()
# counter2 = make_counter()
#
# print(counter())
# print(counter())
# print(counter())

# def sendMsg(userTo):
#     x = 5
#     def setMsg(msgTxt):
#         print("Dear {}, welcome to Python world! {x}".format(userTo, msgTxt))
#
#     return setMsg
#
#
# userAdmin = sendMsg('admin')
# userAdmin("Hello!")
# userAdmin("t2!")
#
# userAdmin = sendMsg('user')
# userAdmin("Hello!")
# userAdmin("t2!")
#
# userAdmin = sendMsg('asdasd')
# userAdmin("Hello!")
# userAdmin("t2!")

# def sendMsg(userTo):
#     def setMsg(msgTxt=''):
#         def setUserFrom(userFrom=''):
#             def setLang(lang=''):
#                 print("Dear {}, Hello from {}. Welcome to {} world! {}".format(userTo, userFrom, lang, msgTxt))
#             return setLang
#         return setUserFrom
#     return setMsg
#
#
# case1 = sendMsg('admin')
# case1('Hello')()

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         res = func(*args, **kwargs)
#         print("End")
#         return res
#     return wrapper
#
#
# @my_decorator
# def foo(name):
#     print("Hello ", name)
#     return "FOO"
#
# print(foo('Alex'))

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return decorator_repeat
#
#
# @repeat(5)
# def foo():
#     print("Hello")
# foo()
# import logging
#
#
# def logger(func):
#     logging.basicConfig(level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         logging.info(f"Called {func.__name__} with {args} and {kwargs}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @logger
# def add(x, y):
#     return x + y
#
# @logger
# def mult(x, y):
#     return x * y
#
#
# add(5, 3)
# mult(2, 1)
# add(7, 3)


# users = {
#     'bob': {'role': 'admin'},
#     'den': {'role': 'user'},
#     'alice': {'role': 'guest'}
# }
#
#
# def role_required(*roles):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             user = kwargs.get('username')
#             user_role = users.get(user, {}).get('role')
#             if user_role not in roles:
#                 print(f"Access denied! User {user} does not have the required role: {roles}")
#                 return
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
# @logger
# @role_required('admin')
# def delete_user(username):
#     print(f"User {username} deleted from database")
#     return 5
#
# @role_required('user', 'admin')
# def buy_item(username):
#     print(f"User {username} bought item..")
#
#
# @role_required('guest', 'user', 'admin')
# def visit_site(username):
#     print(f"User {username} visit site..")
#
#
# visit_site(username='alice')
# delete_user(username='alice')
# buy_item(username='alice')
#
# buy_item(username='den')
#
# delete_user(username='bob')


# Exceptions


# try:
# ...code Exception
# except:
# ...code замість exception
# while True:
#     try:
#         number = int(input("Enter number: "))
#         break
#     except:
#         print("Something went wrong... need enter a number!")
#
#
# print(number == 1)

# try:
#     n1 = int(input("Enter number1: "))
#     n2 = int(input("Enter number2: "))
#     if n2:
#         res = n1 / n2
#         print("Result: ", res)
#     else:
#         raise ZeroDivisionError("Your enter number2 equals zero! ")
# except (ValueError, TypeError) as e:
#     print("ERROR! Your enter not a number! ", e)
# except ZeroDivisionError as e:
#     print("ERROR!", e)
# except Exception as e:
#     print("Unknown error: ", e)
# else:
#     print("The else block")
# finally:
#     print("the finally block")

# print("Continue..")

# def foo(a,b):
#     try:
#         print("Внутрішній блок try")
#         return a/b
#     except ZeroDivisionError as e:
#         print("Обробка винятку! Внутрішній блок except")
#     finally:
#         print("Внутрішній блок finally!")
# try:
#     print("Зовнішній блок try")
#     res = foo(5,"asc") / 0
#
# except Exception as e:
#     print("Обробка винятку! Зовнішній блок except", e)
# finally:
#     print("Зовнішній блок finally!")


# throw

# def validate_age(age):
#     if not age.isdigit():
#         raise ValueError("Введіть вік(числом)!")
#     if int(age) < 0:
#         raise ValueError("Вік не може бути від'ємним")
#     if age > 200:
#         raise ValueError("Введений вік нереалістично великий!")
#     return True
#
# try:
#     age = input("Enter age: ")
#
#     validate_age(age)
# except ValueError as e:
#     print("Помилка валідації: ", e)

# w - overwrite data, if file not exists then create.
# r - read data file, if file not exists - Exception
# a - append data to end the file
# b - binary file
# r+w - read and write, if data not exists - Exception

# try:
# f = open('file.txt', 'r+') w+
# print(repr(f.read()))


# except Exception as e:
#     print(e)
# else:
#     f.close()

# Дан текстовый файл. Необходимо создать новый файл,
# в который требуется переписать из исходного файла все
# слова, состоящие не менее чем из семи букв.
# from string import punctuation
#
# try:
#     with open('input.txt', 'r') as infile, open('output.txt', 'w') as outputfile:
#         text = infile.read()
#         words = text.split()
#         long_words = [word.strip(punctuation) for word in words if len(word.strip(punctuation)) >= 7 and
#                       (word.replace('-', '').strip(punctuation).isalpha())]
#
#         for word in long_words:
#             outputfile.write(word + '\n')
# except Exception:
#     print("Error")


# with

# f = open('x')
#
# f.close()

# with con as c:
# ....c
# try:
#     with open('file.txt') as f:
#         f.read()
#     f.write('sd')
# except Exception:
#     print("")

# Задание 4 Дан текстовый файл. Добавить в него строку из двенадцати звездочек
# (************), поместив ее после последней из строк, в которых нет запятой.
# Если таких строк нет, то новая строка должна быть добавлена после всех строк
# имеющегося файла. Результат записать в другой файл.

# def add_stars(infile, outfile):
#     with open(infile, 'r') as f:
#         lines = f.readlines()
#
#     inx = None
#     for i in range(len(lines)):
#         if ',' not in lines[i]:
#             inx = i
#
#
#     if inx is None:
#         inx = len(lines)
#
#     lines.insert(inx + 1, '******************\n')
#
#     with open(outfile, 'w') as f:
#         f.writelines(lines)
#
#
# add_stars('file.txt', 'output.txt')

# Дан текстовый файл. Переписать в
# другой файл все его строки с заменой в них
# символа * на символ & и наоборот.

# with open('file.txt', 'r') as f:
#     lines = f.readlines()
#
# with open('output.txt', 'w') as f:
#     for line in lines:
#         reps = line.replace('*', '\x00').replace('&', '*').replace('\x00', '&')
#
#         f.write(reps)


# csv, os
# import csv

# data = [
#     ['Name', 'Age', 'City'],
#     ['Den', 20, 'Lviv'],
#     ['Alice', 30, 'New York']
# ]
# data1 = ['Bob',20, 'Lviv']
#
# with open('output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#     writer.writerow(data1)
#
# with open('output.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         print(row)

# data = [
#     {'Name': 'Den', 'Age': 25, 'City': 'Lviv'},
#     {'Name': 'Alice', 'Age': 50, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 20, 'City': 'Lviv'},
# ]
# fieldnames = ['Name', 'Age', 'City']
#
# with open('output.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)
#
# data = {'Name': 'Nick', 'Age': 5, 'City': 'Lviv2'}
# with open('output.csv', 'a', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writerow(data)
#
# with open('output.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f, fieldnames=fieldnames)
#     # header = next(reader)
#     for row in reader:
#         print(row)


# rows = []
# fieldnames = ['Name', 'Age', 'City']
# with open('output.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     # header = next(reader)
#     for row in reader:
#         print(reader.line_num)


# with open('output.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writerows(rows)


import os

# os.mkdir('papka')
# os.rmdir('papka')

# os.rename('papka', 'PAPKA')
# os.remove('papka/file.txt')
# os.rename('papka/new_output.txt', 'X.txt')
# print(os.getcwd())
# print(os.listdir('D:\\Projects\\STEP\\python35'))
# print(os.getenv('TEMP'))
# print(os.putenv('TEMP', '123'))
# os.system('echo Hello')
# print(os.getlogin())
# os.chown()

# path = input("Enter path to directory: ")
#
#
# def list_dir(path, level=0):
#     try:
#         items = os.listdir(path)
#     except PermissionError:
#         return
#     for item in items:
#         item_path = os.path.join(path, item)
#         print('   ' * level + '|--' + item)
#         if os.path.isdir(item_path):
#             list_dir(item_path, level+1)
#
#
# if os.path.exists(path) and os.path.isdir(path):
#     print("Contains directory: ")
#     list_dir(path)
# else:
#     print("Incorrect path!")

# f_path = os.path.join('\\path1\\path\\2', 'path3', 'path4.txt')
# print(f_path)
#
# path = input("Enter path to directory: ")
#
#
# def list_dir(path):
#     for root, dirs, files in os.walk(path):
#         rel_path = os.path.relpath(root, path)
#         level = rel_path.count(os.sep)
#         print("    " * level + "|-- " + os.path.basename(root))
#
#         for file in files:
#             print("    " * (level + 1) + "|-- " + file)
#
#
# if os.path.exists(path) and os.path.isdir(path):
#     print("Contains directory: ")
#     list_dir(path)
# else:
#     print("Incorrect path!")
# Напишіть програму яка буде сканувати вказану директорію
# знаходити файли старіші за певну кількість днів і переміщяти
# їх до архівної директорії

# import os
# import time
# import shutil
#
#
# def archive_old_files(base_directory, days_old, archive_directory):
#     current_time = time.time()
#     age_limit = 1800
#
#     for root, dirs, files in os.walk(base_directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_age = current_time - os.path.getctime(file_path)
#             if file_age > age_limit:
#                 rel_path = os.path.relpath(root, base_directory)
#                 archive_path = os.path.join(archive_directory, rel_path)
#                 os.makedirs(archive_path, exist_ok=True)
#
#                 shutil.move(file_path, os.path.join(archive_path, file))
#
#                 print(f"File {file} moved to {archive_path}")
#
#
# base_directory = input("Enter base directory: ")
# days_old = int(input("Enter days old count: "))
# archive_directory = input("Enter archive directory: ")
#
# if os.path.exists(base_directory) and os.path.isdir(base_directory):
#     print("Contains directory: ")
#     archive_old_files(base_directory, days_old, archive_directory)
# else:
#     print("Incorrect path!")

