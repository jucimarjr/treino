quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de eleitores: '))
    if (quantidade <= 0):
        print ('A quandidade deve ser positiva!')

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
for i in range(0, quantidade):
    voto = 0
    while (voto < 1) or (voto > 3):
        voto = int(input('Você quer votar no candidato 1, 2 ou 3: '))
        if (voto < 1) or (voto > 3):
            print ('Candidato inválido! Vote novamente')
    if (voto == 1):
        votosCandidato1 += 1
    elif (voto == 2):
        votosCandidato2 += 1
    else:
        votosCandidato3 += 1

print ('Resultado:')
print ('Candidato 1:', votosCandidato1)
print ('Candidato 2:', votosCandidato2)
print ('Candidato 3:', votosCandidato3)