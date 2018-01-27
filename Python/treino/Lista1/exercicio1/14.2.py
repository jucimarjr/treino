print ("Exerc 14")

peso_peixe = float(input("Informe o peso dos peixes pescados: "))
pesomaximo = 50
multa = 4

if (peso_peixe > pesomaximo):
 	excesso = (peso_peixe - pesomaximo)
 	print ('Excesso de peso:', excesso)
 	print ('Valor da multa por excesso', excesso * multa)
else:
    print ('Nao houve excesso de peso')
