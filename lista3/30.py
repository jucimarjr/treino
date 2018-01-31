precopao = int(input('Preço do pão: '))

print ('Panificadora  - Tabela de preços')
for i in range(1, 51):
    print ('%d - R$ %.2f' % (i, i * precopao))