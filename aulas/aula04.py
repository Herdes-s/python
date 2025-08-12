# range sequencia do 0 ao 4
for x in range(5):
    print(x)
print('____')

# range sequencia do 2 ao 6
for y in range(2, 7):
    print(y)
print('____')

# range sequencia do 1 ao 11 pulando de 2 em 2
for z in range(1, 11, 2):
    print(z)
print('____')

# continue, pulando o número 5
for x in range(10):
    if x == 5:
        continue
    print(x)
print('____')

# break, interrompe o loop no número 5
for x in range(10):
    if x == 5:
        break
    print(x)
print('____')