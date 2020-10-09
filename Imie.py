# zad 4.
dict_names = {'Patryk': 'męskie',
              'Adam': 'męskie',
              'Krzysztof': 'męskie',
              'Wacław': 'męskie',
              'Dawid': 'męskie',
              'Maja': 'żeńskie',
              'Bartek': 'męskie',
              'Kasia': 'żeńskie',
              'Patrycja': 'żeńskie',
              'Ania': 'żeńskie',
              'Ewa': 'żeńskie',
              'Anna': 'żeńskie',
              'Jagoda': 'żeńskie'}
print(list(dict_names.keys()))
new_name = input('Podaj imie ze zbioru:').capitalize()
if new_name.endswith('a'):
    print(new_name, 'to imie żeńskie')
else:
    print(new_name, 'to imie męskie')
if new_name not in dict_names:
    print('Nie znamy tego imienia')
    gender = input('Podaj czy imie jest męskie lub żeńskie wpisz m/z ')
    if gender == 'm':
        gender = 'męskie'
    elif gender == 'z':
        gender = 'żeńskie'
    else:
        print('Błędna litera podaj ponownie!')
    dict_names[new_name] = gender
print(list(dict_names.keys()))
print(list(dict_names.values()))
