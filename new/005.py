n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
ant = n1 - 1
ant2 = n2 - 1
suc = n1 + 1
suc2 = n2 + 1
s = n1+n2
d = n1/n2
di = n1//n2
e = n1**n2

print('O antecessor de {} é {} e o antecessor de {} é {}!'.format(n1, ant, n2, ant2))
print('O sucessor de {} é {} e o sucessor de {} é {}'.format(n1, suc, n2, suc2))
print('A soma do número {} e {} é igual à {}!'.format(n1, n2, s))
print('A divisão do número {} e {} é igual à {}!'.format(n1, n2, d))
if n1<n2:
    print('Não existe divisão inteira entre {} e {}, pois {} é menos que {}!'.format(n1, n2, n1, n2))
else:
    print('A divisão inteira entre {} e {} é {}!'.format(n1, n2, di))
print('{} elevado à {}  é igual à {}:'.format(n1, n2, e))