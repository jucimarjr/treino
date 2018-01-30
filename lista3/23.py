quantidade = 0
while (quantidade <= 0):
    quantidade = float(input('Você quer saber os primeiros quantos números: '))
    if (quantidade <= 0):
        print ('A quandidade deve ser positiva!')
qd = 0
for numero in range(1, quantidade + 1):
    primo = True
    for c in range(2, numero / 2 + 1):
        qd += 1
        if (numero % c == 0):
            primo = False
            break

    if (primo):
        print (numero,)

print ('\nQuantidade de divisões:', qd)
