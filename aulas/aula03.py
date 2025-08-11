#numero = [1, 2, 3, 5, 7]

#for num in numero:
#    print(num)

numero = int(input('Digite um numero ou 0 para sair:'))
while numero != 0:
    if numero %2 == 0:
        print('O numero é Par!')
    else:
        print('O numero é Impar!')
    numero = int(input('Digite outro numero!'))