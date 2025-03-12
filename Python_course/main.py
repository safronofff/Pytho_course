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

#---Цикл while
