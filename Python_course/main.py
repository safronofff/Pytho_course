#---Данные, типы данных
# n = 1.89
# print(n)
# print(type(n)) # показывает тип данных

# n = 'hello'
# print(n)
# print(type(n))

# m = 'hello \' world' # ковычки
# print(m)

# b = 'hello "beautiful" world' # ковычки
# print(b)

#---Коментарии
# однострочный комментарий
# print(536)

# многострочный комментарий
"""
print(5)
print(5)
print(5)
"""
# комментирование выделением - ctrl+k, ctrl+c
# print(5)
# print(5)
# print(5)
# разкомментирование выделением - ctrl+k, ctrl+u

#---Интерполяция строк
# a = 3
# b = 2.58
# c = 'hello'
# print(a,b,c)
# print(a,' - ', b,' - ', c)
# print(f"{a} - {b} - {c}") # интерпаляция строк
# print("{} - {} - {}".format(a,b,c)) # интерпаляция строк

#---Ввод данных
#input()

# a = input()
# print(a)

# print('enter number: ')
# a = input()
# b = input('enter next number: ')
# print(a)
# print(b)
#--------------
# a = input('enter first number: ')
# b = input('enter two number: ')
# print(a, '+', b, '=', a + b)

#---Приведение типов
# c = 5.89
# print(c)
# n = int(c)
# print(n)
#--------------
# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c + ' - hello!!!')
# print(type(c))
#--------------
# c = 0
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))
#--------------
#Ошибка типов данных
# v = 'hello'
# print(v)
# v = int(v)
# print(v)
#--------------
# a = int(input('enter first number: '))
# b = int(input('enter two number: '))
# print(a, '+', b, '=', a + b)

#---Функция "round"
# a = 5.2563
# b = 4.56487
# print(a * b)
# #round(1.25645, 3) Ф-ция "round" принимает 2 аргумента: 1-число, 2-кол-во знаков после запятой
# print(round(a * b, 3))

#---Сокращенное присваевание
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

#---Логические операции
# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'hello'
# b = 'hello'
# print(a == b)

# a = 1 > 3 > 5 > 7 > 9
# print(a)

# b = 1 < 3 < 5 < 7 < 9
# print(b)

#---Управляющие конструкции if, if-else
# username = input('enter your name: ')
# if username == 'Маша':
#     print('Ура! Это Маша!!!')
# elif username == 'Юра':
#     print('Привет Юра!!!')
# elif username == 'Аня':
#     print('Анюта, рада тебя видеть!!!!!!')
# else:
#     print('привет ', username)
#-------------------------------
# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')

#---Цикл while
# Сумма 3 чисел
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)

#---Конструкция While-else
# i = 0
# while i < 5:
#     if i == 3:
#         break # Оператор break останавливает цикл при достижении определенных условий
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)
# # Но в ООП оператор break отсутствует и его исп. не желательно
#-----------------------
# i = 0
# while i < 5:
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)
#----------------------
# На замену оператору break приходит "метод флажка"
# Данна программа находит минимальный делитель данного числа
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1
#---
# n = int(input("enter number: "))
# flag = True
# i = 2
# while flag: # flag == True
#     if n % i == 0: # если остаток деления числа n на i равен 0
#         flag = False
#         print(f'n % i = {n % i}')
#         print(f'i = {i}')
#     elif i > n // 2: # делитель числа не может привышать введенное число, деленное на 2
#         print(f'n // 2 = {n //2}')
#         print(f'n = {n}')
#         flag = False
#     i += 1

#---Цикл for, функция range()
# функция range принимает 3 аргумента: 
# 1-с какого числа начинаем (range(5)); 
# 2-каким числом заканчиваем (range(5,2)); 
# 3-шаг выполнения(range(1,10,2)) - 1, 3, 5, 7, 9
#---
# a = 'qwerty'
# print(a[0]) # q
# print(a[2]) # e
#---
# a = 'qwerty'

# for i in a:
#     print(i)
#---
# Вложенный цикл
# line = ''
# for i in range(5):
#     line = ''
#     for j in range(5):
#         line += '*'
#     print(line)

#---Строки
# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(len(text)) # Выводит кол-во символов в строке
# print('еще' in text) # Поиск запрашиваемого символа
# print(text.lower()) # Переводит все символы в нижний регистр
# print(text.upper()) # Переводит все символы в верхний регистр
# print(text.replace('еще','КАК МОЖНО БОЛЬШЕ')) # Замена символов на запрашиваемый

#---Срезы
# Срезы очень похожи на ф-цию range
# Мы так же можем передавать 3 эл-та:
# 1 - где начинаем
# 2 - где заканчиваем
# 3 - шаг

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...