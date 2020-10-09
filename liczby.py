# zad 3.
x = float(input('Pierwsza liczba: '))
y = float(input('Druga liczba: '))
z = float(input('Trzecia liczba: '))
##################################################
if x > y and x > z:
    print('Największa liczba to: {}'.format(x))
if x > y > z:
    print('{},''{},''{},'.format(x, y, z))
elif x > z > y:
    print('{},''{},''{},'.format(x, z, y))
##################################################
if y > x and y > z:
    print('Największa liczba to: {}'.format(y))
if y > x > z:
    print('{},''{},''{},'.format(y, x, z))
elif y > z > x:
    print('{},''{},''{},'.format(y, z, x))
##################################################
if z > x and z > y:
    print('Największa liczba to: {}'.format(z))
if z > x > y:
    print('{},''{},''{},'.format(z, x, y))
elif z > y > x:
    print('{},''{},''{},'.format(z, y, x))
