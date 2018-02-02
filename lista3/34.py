n = int(input('Digite um número: '))
i = 0
for c in range(1, n+1):
    if (n/c).is_integer():
        print(n, 'divisivel por', c)
        i += 1
if i <= 2:
    print('{} é primo!'.format(n))
else:
    print('{} não é primo...'.format(n))
