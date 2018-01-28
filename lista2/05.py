nota = int(input("Informe sua primeira nota: "))
nota2 = int(input("Informe sua segunda nota: "))

if ((nota+nota2)/2 == 10):
    print("Aprovado com distinção")
elif((nota+nota2)/2 >= 7):
    print("A média do aluno é:",(nota+nota2)/2,"APROVADO")
else:
     print("A média do aluno é:",(nota+nota2)/2,"REPROVADO")
