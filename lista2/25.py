print ('Responda as perguntas abaixo com [S] Sim ou [N] Não ')

telefonou = input('Você telefonou para a vitima? ').upper()
localCrime = input('Você esteve no local do crime? ').upper()
moraPerto = input('Você mora perto da vitima? ').upper()
devia = input('Você devia para a vitima? ').upper()
trabalhou = input('Você trabalhou para a vitima? ').upper()

classificacao = 0

if (telefonou == 'S'):
    classificacao += 1

if (localCrime == 'S'):
    classificacao += 1

if (moraPerto == 'S'):
    classificacao += 1

if (devia == 'S'):
    classificacao += 1

if (trabalhou == 'S'):
    classificacao += 1

if (classificacao < 2):
    print ('Inocente')
elif (classificacao == 2):
    print ('Suspeito')
elif (classificacao <= 4):
    print ('Cumplice')
else:
    print ('Assassino')
