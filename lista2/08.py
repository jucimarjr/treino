print ("Exerc 08")

preco1 = int(input("Informe o preço do primeiro produto: "))
preco2 = int(input("Informe o preço do segundo produto: "))
preco3 = int(input("Informe o preço do terceiro produto: "))

if (preco1 == preco2) and (preco1 == preco3):
    print ("Pode comprar qualquer coisa, pois eles tem o mesmo preço")
elif (preco1 < preco2) and (preco1 < preco3):
    print ("Compre o primeiro produto")
elif (preco2 < preco3):
    print ("Compre o segundo produto")
else:
    print ("Compre o terceiro produto")
