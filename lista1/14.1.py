print ("Exerc 14")

peso_peixe = int(input("Informe o peso dos peixes pescados: "))
pesomaximo = 50
multa = 4

if (peso_peixe > pesomaximo):
   excesso_de_peixe = (peso_peixe - pesomaximo)
print("Você excedeu o peso do pescado em: ",excesso_de_peixe,"kgs")
print("Você irá pagar uma multa de",excesso_de_peixe*multa,"reais")

elif:(peso_peixe < pesomaximo):
    falta = (pesomaximo - peso_peixe)
print("Ainda falta",falta,"kgs para você chegar no peso máximo")

else:
    print("Você não ultrapassou o máximo permitido")
