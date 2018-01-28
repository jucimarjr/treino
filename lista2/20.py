nota1 = float(input('Qual sua primeira nota?: '))
nota2 = float(input('Qual sua segunda nota?: '))
nota3 = float(input('Qual sua terceira nota?: '))

media = (nota1 + nota2 + nota3) / 3.0

print ("Media do aluno: {}".format(media))
if (media == 10):
    print ('Aprovado com Distinção')
elif (media >= 7):
    print ('Aprovado')
else:
    print ('Reprovado')
