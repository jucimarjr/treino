usuario = senha = ''
while (usuario == senha):
    usuario = input("Informe um nickname: ")
    senha = input("Informe a senha: ")
    if (usuario == senha):
        print ("A senha não pode ser igual ao nickname")
