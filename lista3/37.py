codigo = -1
totalClientes = 0
somaAlturas = 0.0
somaPesos = 0.0
while (codigo != 0):
    codigo = int(input('Informe o código do cliente: '))
    if (codigo != 0):
        altura = float(input('Informe a altura do cliente: '))
        peso = float(input('Informe o peso do cliente:'))
        totalClientes += 1
        somaAlturas += altura
        somaPesos += peso
        if ('maisAlto' not in vars()) or (altura > maisAlto):
            maisAlto = altura
            codigoMaisAlto = codigo
        if ('maisBaixo' not in vars()) or (altura < maisBaixo):
            maisBaixo = altura
            codigoMaisBaixo = codigo
        if ('maisGordo' not in vars()) or (peso > maisGordo):
            maisGordo = peso
            codigoMaisGordo = codigo
        if ('maisMagro' not in vars()) or (peso < maisMagro):
            maisMagro = peso
            codigoMaisMagro = codigo

print ('O cliente mais alto é o de código %i com %f' %\
    (codigoMaisAlto, maisAlto))
print ('O cliente mais baixo é o de código %i com %f' %\
    (codigoMaisBaixo, maisBaixo))
print ('O cliente mais magro é o de código %i com %f' %\
    (codigoMaisMagro, maisMagro))
print ('O cliente mais gordo é o de código %i com %f' %\
    (codigoMaisGordo, maisGordo))

print ('Média da altura dos clientes: %.2f' %\
    (somaAlturas / float(totalClientes)))
print ('Média dos pesos dos clientes: %.2f' %\
    (somaPesos / float(totalClientes)))