# -*- coding: utf8 -*-'


def choose():
    choice = int(input('Wybierz operacje liczbową '))
    if choice == 1:
        print(suma())
    elif choice == 2:
        print(roznica())
    elif choice == 3:
        print(iloczyn())
    elif choice == 4:
        print(iloraz())


def suma():
    x = float(input('Pierwsza liczba '))
    y = float(input('Druga liczba '))
    return x + y


def roznica():
    x = float(input('Pierwsza liczba '))
    y = float(input('Druga liczba '))
    roz = x - y
    return roz


def iloczyn():
    x = float(input('Pierwsza liczba '))
    y = float(input('Druga liczba '))
    ilocz = x * y
    return ilocz


def iloraz():
    x = float(input('Pierwsza liczba '))
    y = float(input('Druga liczba '))
    ilor = x / y
    return ilor


choose()
