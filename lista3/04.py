popuA = 80000
popuB = 200000
cresA = 1.03
cresB = 1.015

#Calculo Anos

ano = 1
while (popuA <= popuB):
    popuA*=cresA
    popuB*=cresB
    ano+=1
#Imprime resultado
    print("Serão necessarios", ano, "anos para que a populacao do pais A ultrapasse a populacao do pais B")
