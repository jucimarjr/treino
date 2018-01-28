print ("Exerc06")

num1 = int(input("Informe um número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if (num1 == num2) and (num1 == num3):
    print ("Os números são iguais")
elif(num1 > num2) and (num1 > num3):
    print ("O maior número é",num1,",o primeiro")
elif(num2 > num3):
    print ("O maior número é",num2,",o segundo")
else:
    print("O maior número é",num3,",o terceiro")
