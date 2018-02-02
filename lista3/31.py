soma = 0.0
quantidade = 1
precomercadoria = 1
while (precomercadoria != 0):
    precomercadoria = float(input('Produto %d: R$ ' % (quantidade)))
    soma += precomercadoria

print ('Total: R$ %.2f' % soma)
pagamento = float(input('Dinheiro: R$ '))

print ('Troco: R$ %.2f' % (pagamento - soma))