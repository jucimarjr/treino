salario = float(input("Informe o salário: "))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
novosalario = salario + aumento

print ("Salário antes do ajuste:", salario)
print ("Percentual de aumento", percentual, '%')
print ("Valor do aumento:", aumento)
print ("Novo salário:", novosalario)
