quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Você quer informar quantos numeros: '))
    if (quantidade <= 0) :
        print ('Quantidade deve ser positiva!')
    elif (quantidade > 1000):
        print ('Quantidade deve ser menor que 1000')

soma = 0
for i in range(0, quantidade):
    numero = int(input('Informe um numero: '))
    if ('maior' not in vars()) or (numero > maior):
        maior = numero

    if ('menor' not in vars()) or (numero < menor):
        menor = numero

    soma += numero

print ('Menor numero:', menor)
print ('Maior numero:', maior)
print ('Soma dos numeros:', soma)