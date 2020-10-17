# -*- coding: utf8 -*-'
a = int(input('Pierwsza liczba '))
b = int(input('Druga liczba '))
choose = int(input('Wybierz operacje liczbową '))


def choice():
    if choice == 1:
        suma(a, b)
    if choice == 2:
        roznica(a, b)
    if choice == 3:
        iloczyn(a, b)
    if choice == 4:
        iloraz(a, b)


def suma(a, b):
    summ = a + b
    print(summ)
    return summ


def roznica(x, y):
    roz = x - y
    return roz


def iloczyn(x, y):
    ilocz = x * y
    return ilocz


def iloraz(x, y):
    ilor = x / y
    return ilor
