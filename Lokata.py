# -*- coding: utf8 -*-


start = int(input("stan konta? "))
rate = int(input("Ile lat na lokacie? "))
n = float(input("Stopa oprocentowania w skali roku? "))
wynik = start*(1+rate*n)
print("Po {} latach kapitał będzie wynosił {:.2f}zł" .format(rate, wynik))

start = float(input("Stan początkowy konta wynosi: "))

# np. stopa oprocentowania 6% = 0.06
rate = float(input("Stopa oprocenotowania w skali roku: "))

n = int(input("Liczba lat na lokacie: "))
end = start*(1 + rate*n)

print("Po {} latach kapitał będzie wynosił {} zł".format(n, end))
