popuA= 0
cresA= 0

#Valor das populações e taxas de crescimento
while (popuA <=0):
    popuA = int(input("Informe a população do país A: "))
    if (popuA <=0):
        print ("População deve ser um valor positivo")
while (cresA <= 0):
    cresA = float(input("Informe o percentual de crescimento do país A: "))
    if (cresA <=0):
        print("O percentual do crescimento deve ser um valor positivo")
popuB = popuA
while (popuB <= popuA):
    popuB = int(input("Informe a população do país B: "))
    if (popuB <= popuA):
        print ("População do país B deve ser maior que a população do país A")
cresB = cresA
while (cresB >= cresA):
    cresB = float(input("Informe o percentual de crescimento do país B: "))
    if (cresB >= cresA):
        print ("O percentual do crescimento do país B deve ser menor que do país A")

cresA = 1 + (cresA / 100)
cresB = 1 + (cresB / 100)

ano = 1
while (popuA <= popuB):
    popuA *= cresA
    popuB *= cresB
    ano += 1

# Imprime o resultado
print ('Serão necessários', ano, 'anos para que a populção do pais A '\
    'ultrapasse a populacao do pais B')
