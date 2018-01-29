print ('Digite 10 números')
pares = 0
impares = 0
for i in range(1, 11):
    num = int(input('Digite um número: '))
    if (num % 2 == 0):
        pares += 1
    else:
        impares += 1

print ('Números pares:', pares)
print ('Números impares:', impares)
