# if-elif-else

a = input('enter time o clock: ')

a = int(a)

if a != 0:
    if a < 6:
        print(f'time {a} is night')
    elif a > 6 and a <= 12:
        print(f'time {a} is morning')
    elif a > 12 and a <= 18:
        print(f'The time {a} is day')
    elif a > 18 and a <= 23:
        print(f'The time {a} is evening')
elif a == 0:
    print(f'The time {a} is midnight')
elif a > 24:
    print('incorrect data')