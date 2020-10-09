seriale = {'the walking dead': 8.2,
           'orange is the new black': 8.1,
           'breaking bad': 8.3,
           'lost': 9.6,
           'prison break': 9.2,
           'chernobyl': 0,
           'klan': 4.6,
           'Świat według Kiepskich': 7.3,
           'Gra o Tron': 8.8,
           'Dom z papieru': 8.9
           }
print(list(seriale.keys()))
name = input('Jaki serial chcesz wybrać? ')
print('Serial {} ma ocene {}' .format(name, seriale[name]))
new = input('Dodaj kolejny serial do listy ')
rate = input('Jaka ocene ma?'+new+'?')
seriale[new] = float(rate)
print(list(seriale.keys()))
print(list(seriale.values()))
