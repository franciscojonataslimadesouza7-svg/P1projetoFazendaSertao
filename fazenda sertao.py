usuarios = [
    ["jonatas", "1234", "ADM"],
    ["joao", "12", "CLIENTE"]
]

while True:
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # CADASTRO
    if opcao == "1":
        login = input("Login: ")

        while True:
            senha = input("Senha: ")

            if len(senha) >= 8:
                break
            else:
                print("Senha invalida! (minimo 8 caracteres)")

        perfil = input("Perfil (ADM ou CLIENTE): ").upper()

        usuarios.append([login, senha, perfil])
        print("Usuario cadastrado!")

    # LOGIN (SEM FOR)
    elif opcao == "2":
        login = input("Login: ")
        senha = input("Senha: ")

        if usuarios[0][0] == login and usuarios[0][1] == senha:
            print("Login realizado!")
            print("Perfil:", usuarios[0][2])

        elif usuarios[1][0] == login and usuarios[1][1] == senha:
            print("Login realizado!")
            print("Perfil:", usuarios[1][2])

        else:
            print("Login invalido!")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida!")