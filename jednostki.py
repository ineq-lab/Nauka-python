# -*- coding: utf8 -*-
cm = int(input("Podaj długość w cm: "))
cm_to_m = cm/100
cm_to_cal = cm/0.394

print("Długość {} cm to {} metrów lub {:.3f} cali".format(cm, cm_to_m, cm_to_cal))

zl = float(input('Ile masz pieniędzy?'))
funt = 0.20*zl
euro = 0.22*zl
dolar = 0.26*zl
print("W Angli bedziesz mieć {:.2f} w Euro {:.2f} a w Stanach {:.2f} dolarów".format(funt, euro, dolar))
