num = int(input('Informe o número que você quer ver a tabuada: '))

print ('Tabuada de', num, ':')
for i in range(1, 11):
    print (num, 'X', i, '=', (num * i))
