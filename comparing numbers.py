# if-elif-else

a = input('enter first number: ')
b = input('enter two number: ')
c = input('enter tree number: ')

a = int(a)
b = int(b)
c = int(c)

if a != b and a != c and b != c:
    if a > b > c:
        print(a, '>', b, '>', c)
    elif a > b < c:
        print(a, '>', b, '<', c)
    elif a < b > c:
        print(a, '<', b, '>', c)
    else:
        print(a, '<', b, '<', c)
elif a != b or a != c or b != c:
    if a > b == c:
        print(a, '>', b, '==', c)
    elif a < b == c:
        print(a, '<', b, '==', c)
    elif a == b > c:
        print(a, '==', b, '>', c)
    else:
        print(a, '==', b, '<', c)
else:
    print(a, '==', b, '==', c)