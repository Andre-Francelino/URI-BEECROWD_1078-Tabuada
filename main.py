#URI-BEECROWD 1078 - Tabuada

n = int(input("Calcular tabuada do número: "))

for cont in range(1, 11):
    print('{} x {} = {}'.format(cont, n, cont * n))

