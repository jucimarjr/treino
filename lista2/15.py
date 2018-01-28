lado1 = int(input("Informe o valor do primeiro número: "))
lado2 = int(input("Informe o valor do segundo número: "))
lado3 = int(input("Informe o valor do terceiro número: "))

# Verifica se é um triangulo
if (lado1 > (lado2 + lado3)) or (lado2 > (lado1 + lado3))\
        or (lado3 > (lado1 + lado2)):
    eTriangulo = False
else:
    eTriangulo = True

if (eTriangulo):
    print ("Dá pra formar um triângulo")
    # Verifica o tipo de triangulo
    if (lado1 == lado2) and (lado2 == lado3):
        print ('Equilátero')
    elif (lado1 == lado2) or (lado1 == lado2) or (lado2 == lado3):
        print ('Isosceles')
    else:
        print ('Escaleno')
else:
    print ("Os valores não formam um triângulo :/")
