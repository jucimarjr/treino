a = int(input('Digite o numero: '))
tot = 0
for cont in range(1, a + 1):
    if a % cont == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(cont), end=' ')
print('\n\033[m{} é divisel {} vezes'.format(a, tot))
if tot == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO!')﻿
