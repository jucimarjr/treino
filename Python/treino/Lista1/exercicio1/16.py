print ("Exerc 16")
tamanho = float(input("Qual o tamanho em metros quadrados da área a ser pintada?: "))
litro = tamanho/3
latas = int(litro/18)
if (litro % 18 != 0):
    latas+=1
print ("Você devera comprar", latas, "latas.'")
print ("O valor a pagar é de", latas*80,)

            
