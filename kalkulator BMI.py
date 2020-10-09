# -*- coding: utf8 -*-'
wzrost = float(input(u'Twój wzrost w cm:'))/100
masa = float(input('Twoja waga w kg:'))
BMI = masa/wzrost**2
print("Twoje BMI wynosi: {:.2f}".format(BMI))
print('Twoje BMI to:', round(BMI, 3))
if BMI < 18.5:
    print('Niedowaga')
elif 18.5 <= BMI < 24:
    print('Waga normalna')
elif 24 <= BMI <= 26.5:
    print('Lekka nadwaga')
elif 26.5 < BMI <= 30:
    print('Nadwaga')
elif 30 < BMI < 35:
    print('Otyłość I stopnia')
elif 35 <= BMI <= 40:
    print('Otyłość II stopnia')
elif BMI > 40:
    print('Otyłość III stopnia')
