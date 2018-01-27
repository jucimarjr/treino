print ("Exerc 17")
tamanho = float(input("Qual o tamanho em metros quadrados da área a ser pintada?: "))
litros = tamanho/6
latas = int(litros/18)
galoes = int(litros/3.6)

# Calculo de latas
if (litros % 18 != 0):
    latas +=1

# Calculo de galoes
if (litros % 3.6 != 0):
    galoes+=1

print ('Número de latas:', latas, '. Valor:', latas * 80)
print ('Número de galões:', galoes, '. Valor:', galoes * 25)
