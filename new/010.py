print('='*12)
print('Conversor real para dólar')
d = float(input('Digite o valor atual do dólar: '))
r = float(input('Digite quanto você tem em reais: '))
print('Você pode comprar ${:.2f} dólares com R${:.2f} reais!!'.format((r/d), r))
print('='*12)
