strin = '_zmęczony jestem JAK pies_'
seq = '1234'
digital = (5, 23, 9, 150, 2094, 305, 1409, 78)
txt = ('Serwetka', 'Nożyce', 'Papier', 'Kufel', 'Ambrozja', 'Wykaz')
message = 'wiadomośćzostaławysłana'
none = "   "
reward = 'Nadchodzi Wielka Wojna'
print(strin.lower())  # obniża
print(strin.upper())  # podwyższa
print(strin.swapcase())  # swapuje(odwraca)
print(strin.capitalize())  # kapitał pierwszej litery na dużą
print(strin.title())  # tytułuje tekst
print(' '.join(strin))  # dodaje do kazdego znaku
print(strin.lstrip('_zmęczony'))  # usuwa z lewej strony
print(strin.rstrip('pies_'))  # usuwa z prawej strony
print(strin.strip('_'))  # usuwa z obydwu stron
print('Maksymalny string txt:', max(txt), '\nMaksymalna liczba digital:', max(digital))  # zwraca najwyższy string
print('Minimalny string txt:', min(txt), '\nMinimalna liczba digital:', min(digital))  # zwraca najniższy string
print('Długość znaków dla string:', len(strin))
print(strin.split())  # rozdziela string na stringi na liste
print(strin.splitlines())  # robi z stringu liste
print(strin.replace('jestem', 'bardzo jestem'))  # zamienia stary string na nowy replace(old,new)
print('*' * 40)
print(strin.count('e', 10, 18))  # zlicza ile razy wystąpi znak e od indeksu 10 do 18
print(strin.find('t', 0, 14))  # znajduje nr indeksu występowania znaku
print(strin.rfind('s_'))  # znajduje nr indesku reverse licząć od końca
print(strin.index('o', 0, 7))  # znajduje nr indeksu wystawia błąd gdy nie ma str
print(strin.rindex('A', 0, 20))  # znajduje nr indesku od końca wystawia błąd
print("*" * 40)
print(none.isalnum())  # zwraca True jeśli wszystkie znaki to cyfry or alfanumeryczne
print(message.isalpha())  # zwraca True jeśli wszystkie znaki są literami
print(seq.isdigit())  # zwraca True jeśli wszystkie znaki to cyfry
print(message.islower())  # zwraca true jeśli wszystkie znaki są małymi literami
print(none.isspace())  # zwraca true jeśli wszystkie znaki to whitespace
print(reward.istitle())  # zwraca true jeśli ciąg znaków to tytuł
print(reward.isupper())  # zwraca true gdy stringi są dużymi literami
print(message.startswith('wia', 0, 23))  # zwraca true jeśli string zaczyna sie od początku indeksu
print(message.endswith('na', 0, 23))  # zwraca true jeśl string kończy sie na końcu indeksu
