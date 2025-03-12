# if-elif-else

print('Welcome to fuel station!')
print('select the fuel name: 92 or 95 or DT?')
fuel = input('enter the name of the fuel: ')
liters = int(input('enter the number of liters: '))

if fuel == '92':
    a = 50
    fuel == a
    fuel == int(a)
    print(f'The cost of fuel 92 is = {a * liters} dollars.')
elif fuel == '95':
    a = 55
    fuel == a
    fuel == int(a)
    print(f'The cost of fuel 95 is = {a * liters} dollars.')
elif fuel == 'DT':
    a = 60
    fuel == a
    fuel == int(a)
    print(f'The cost of fuel DT is = {a * liters} dollars.')
else:
    print('You entered the wrong fuel name.')
    print('Re-enter the fuel name!')