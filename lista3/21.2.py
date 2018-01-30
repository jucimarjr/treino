n = int(input('Digite um número inteiro: '))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
       c += 1
if c == 2:
    print(' O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
