print ("Exerc 13")

altura = float(input("Informe a sua altura: "))
sexo = (input("Informe seu sexo (M/F): "))
peso = float(input("Informe seu peso atual: "))

if (sexo == "M"):
    peso_ideal = ((72.7*altura) - 58)

else: peso_ideal = (62.1*altura) - 44.7

if (peso > peso_ideal):
    print(" Você está acima do peso ideal",peso_ideal,'kg')

elif(peso < peso_ideal):
    print ("Você está abaixo do peso ideal", peso_ideal,"kg")

else :

    print(" Você está com o peso ideal")
    
