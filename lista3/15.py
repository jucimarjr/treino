numero = int(input('Quantos termos você quer mostrar? '))

cont = 0
anterior = 0
atual = 1
proximo = 1

print('~' * 30)
while cont != numero - 1:
    if cont == 0:
        print(cont, '-> ', end='')
    print('{} -> '.format(proximo), end='')
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    cont = cont + 1

