num = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('*', end='')
    print('{} '.format(c), end='')
print('\n Os números indicados com (*) são os seus divisores')
