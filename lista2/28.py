# Escolha do tipo de grão
print ('1 - Feijão')
print ('2 - Lentilha')
print ('3 - Soja')
tipograo = input('Informe o tipo de grão escolhido: ').upper()

# Escolha da quantidade
quantidade = float(input('Informe a quantidade comprada: '))

# Verifica cartao
cartaodb = input('Usara cartão DB (S/N): ').upper()

print ('CUPOM FISCAL')

# Verifica o tipo da carne e calcula o valor bruto
if (tipograo == '1'):
    print ('Grão Escolhido: Feijão')
    if (quantidade <= 5):
        valorBruto = quantidade * 4.9
    else:
        valorBruto = quantidade * 5.8
elif (tipograo == '2'):
    print ('Grão Escolhido: Lentilha')
    if (quantidade <= 5):
        valorBruto = quantidade * 5.9
    else:
        valorBruto = quantidade * 6.8
else:
    print ('Grão Escolhido: Soja')
    if (quantidade <= 5):
        valorBruto = quantidade * 6.9
    else:
        valorBruto = quantidade * 7.8
print ('Valor Bruto', valorBruto,'reais')

# Verifica se possui desconto
desconto = 0.0
if (cartaodb == 'S'):
    print ('Pagamento com cartão DB')
    desconto = valorBruto * 0.05
else:
    print ('Pagamento não será com o cartão DB')
print ('Desconto: ', desconto,'reais')
print ('Valor a Pagar: ', (valorBruto - desconto),'reais')
