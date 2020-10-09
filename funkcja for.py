z = int(input('Ile razy powtarzać program? '))
for j in range(1, z + 1):
    x = int(input('Podaj liczbe '))
    for i in range(1, x + 1):
        if i % 3 == 0:
            print(i, "\tLiczba jest wielokrotnośćią 3")
        if i % 4 == 0:
            print(i, '\tLiczba jest wielokrotnością 4')
        if i % 4 == 0 and i % 3 == 0:
            print(i, '\tHurra!!')
        else:
            print(i, '\t*')
