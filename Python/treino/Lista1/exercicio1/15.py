print ("Exerc 15")

valor_hora = int(input('Quanto você ganha por hora ? '))
hora = int(input('Por quantas horas você trabalha por mês? '))
SB = valor_hora*hora
IR = SB*0.11
inss = SB*0.08
sind = SB*0.05
SL = SB - IR - inss - sind
print ("Você pagou",IR,"reais em imposto de renda")
print ("Você pagou",inss,"reais em INSS")
print ("Você pagou",sind,"reais em sindicato")
print ("Você ganha o equivalente a: ",SB,"reais em salário bruto")
print ("Você ganha o equivalente a: ",SL,"reais em salário liquido") 
