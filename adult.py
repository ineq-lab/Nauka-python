# zad 1.
age = int(input('Ile masz lat? '))
adult = 18 - age
if age < 18:
    print('Uźytkownik niepełnoletni')
    print('Pozostało {} lat do pełnoletności' .format(adult))
elif age >= 18:
    print('Uźytkownik pełnoletni')
if age > 100:
    print('200 lat! 200 lat! niech żyje żyje nam!')