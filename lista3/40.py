somaVeiculos = 0
somaAcidentes = 0
somaAcidentesMenos2Mil = 0
totalCidadesMenos2Mil = 0

for i in range(0, 2):
    codigo = int(input('Informe o código da cidade: '))
    veiculos = int(input('Informe o número de veiculos de passeio: '))
    acidentes = int(input('Informe a quantidade de acidentes em 1999: '))

    indiceA = acidentes / float(veiculos)
    somaVeiculos += veiculos

    if ('maisAcidentes' not in vars()) or (indiceA > maisAcidentes):
        maisAcidentes = indiceA
        codigoMaisAcidentes = codigo
    if ('menosAcidentes' not in vars()) or (indiceA < menosAcidentes):
        menosAcidentes = indiceA
        codigoMenosAcidentes = codigo

    if (veiculos < 2000):
        somaAcidentesMenos2Mil += acidentes
        totalCidadesMenos2Mil += 1

print ('O cidade com maior indice de acidentes eh %i com %.2f' %\
    (codigoMaisAcidentes, maisAcidentes))
print ('O cidade com menor indice de acidentes eh %i com %.2f' %\
    (codigoMenosAcidentes, menosAcidentes))
print ('A média de veículos nas cidades é %.2f' % (somaVeiculos / 5.0))
print ('A média de acidentes de trânsito nas cidades com menos '\
    'de 2.000 veiculos eh %.2f' %\
    (somaAcidentesMenos2Mil / float(totalCidadesMenos2Mil)))