print('Calcule a média do aluno')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1+n2)/2
print('A média do aluno é {}'.format(media))
if media < 7:
    print('O aluno não foi aprovado')
else:
    print('O aluno foi aprovado')

