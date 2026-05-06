usuarios = [
    ["jonatas", "1234", "ADM"],
    ["joao", "12345678", "CLIENTE"]
]

while True:

    print("\n--- MENU ---")
    print("1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # =========================
    # CADASTRO
    # =========================
    if opcao == "1":

        login = input("Novo login: ")

        while True:

            senha = input("Nova senha: ")

            if len(senha) >= 8:
                break

            else:
                print("Senha invalida!")

        usuarios.append([login, senha, "CLIENTE"])

        print("Usuario cadastrado!")

    # =========================
    # LOGIN
    # =========================
    elif opcao == "2":

        login = input("Login: ")
        senha = input("Senha: ")

        encontrou = False

        for u in usuarios:

            if u[0] == login and u[1] == senha:

                encontrou = True

                print("\nLogin realizado!")
                print("Perfil:", u[2])

                # =========================
                # AREA DE COMPRA
                # =========================
                while True:

                    produto = input(
                        "\nQUAL PRODUTO VOCE QUER COMPRAR?: "
                    ).upper()

                    quantidade = int(
                        input("QUANTIDADE DE PRODUTOS: ")
                    )

                    data = input(
                        "DATA RETIRADA(dd/mm/aaaa): "
                    )

                    hora = input(
                        "HORA RETIRADA (hh:mm:ss): "
                    )

                    print(
                        f"\nAgendamento feito! "
                        f"Produto: {produto} | "
                        f"Quantidade: {quantidade}"
                    )

                    print(
                        f"Data: {data} | Hora: {hora}"
                    )

                    continuar = input(
                        "\nDeseja fazer outra compra? (s/n): "
                    ).upper()

                    if continuar == "S":
                        continue

                    elif continuar == "N":
                        print("Logout realizado!")
                        break

                    else:
                        print("Opcao invalida!")
                        break

                # IMPORTANTE
                break

        if encontrou == False:
            print("Login invalido!")

    # =========================
    # SAIR
    # =========================
    elif opcao == "0":

        print("Saindo...")
        break

    else:
        print("Opcao invalida!")