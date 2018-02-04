for i in range(0, 3):
    codigo = int(input('Informe o código do aluno: '))
    altura = int(input('Informe a altura do aluno em cm: '))
    if ('maisAlto' not in vars()) or (altura > maisAlto):
        maisAlto = altura
        codigoMaisAlto = codigo
    if ('maisBaixo' not in vars()) or (altura < maisBaixo):
        maisBaixo = altura
        codigoMaisBaixo = codigo

print ('O aluno mais alto eh o de código %i com %f' %\
       (codigoMaisAlto, maisAlto))
print ('O aluno mais baixo eh o de código %i com %f' %\
       (codigoMaisBaixo, maisBaixo))