# -*- coding: utf8 -*-
# zad 5.
A = int(input('Długość boku A: '))
B = int(input('Długość boku B: '))
C = int(input('Długość boku C: '))
numbers = [A, B, C]
numbers.sort()
print(numbers)
if A + B > C:
    print('Da sie utworzyć Trójkąt')
    triangle = True
else:
    print('Nie da sie utworzyć trójkąta')
    triangle = False
if triangle and A ** 2 + B ** 2 == C ** 2:
    print('to trójkąt pitagorejski')
    if numbers == [3, 4, 5]:
        print('Trójkąt jest trójkątem pitagorejskim i egpiskim')
elif triangle:
    print('Trójkąt,ale nie pitagorejski')
