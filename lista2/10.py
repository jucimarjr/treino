print ("Exerc 10")

print ("Qual turno você trabalha")
print ("[M] para Matutino")
print ("[V] para Vespertino")
print ("[N] para Noturno")
turno = input(" Escolha uma das opções acima: ")

if (turno == 'M'):
    print ("Bom dia!")
elif (turno == 'V'):
    print ("Boa tarde!")
elif (turno == 'N'):
    print ("Boa noite!")
else:
    print ("Escolha alguma das três opções")
