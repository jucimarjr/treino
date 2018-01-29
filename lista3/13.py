base = int(input('Informe o valor da base: '))
exp = 0
while (exp <= 0):
    exp = int(input('Informe o valor do expoente: '))
    if (exp <= 0):
        print ('O expoente deve ser positivo')

potencia = 1
for i in range(1, exp + 1):
    potencia *= base

print (base, 'elevada a', exp, '=', potencia)
