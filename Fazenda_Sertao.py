# Lista inicial de usuários com login, senha e perfil
usuarios = [
    ["jonatas", "123", "ADM"],
    ["maria", "abc", "CLIENTE"]
]

# Lista de animais cadastrados
animais = []

# Loop principal do sistema
while True:
    print("\n-------- MENU --------")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Login")
    print("0 - Sair")

    opcao = input("Escolha (1, 2, 3, 0): ").strip()

    # CADASTRAR NOVO USUÁRIO
    if opcao == "1":
        print("\n--- CADASTRO ---")
        login = input("Digite o login: ").strip()
        senha = input("Digite a senha: ").strip()
        perfil = input("Digite o perfil (ADM ou CLIENTE): ").strip().upper()

        usuarios.append([login, senha, perfil])
        print("Usuário cadastrado com sucesso!")

    # LISTAR USUÁRIOS
    elif opcao == "2":
        print("\n--- USUÁRIOS ---")
        for u in usuarios:
            print(f"Login: {u[0]} | Perfil: {u[2]}")

    # # LOGIN
    # elif opcao == "3":
    #     print("\n--- LOGIN ---")
    #     login = input("Login: ").strip()
    #     senha = input("Senha: ").strip()
    #
    #     encontrado = None
    #     for u in usuarios:
    #         if u[0] == login and u[1] == senha:
    #             encontrado = u
    #             break

        if encontrado:
            print("Login realizado com sucesso!")
            perfil = encontrado[2]

            # ================= ADM =================
            if perfil == "ADM":
                print("BEM VINDO ADM")

                while True:
                    print("\n--- MENU ADM ---")
                    print("3 - Cadastrar animal")
                    print("4 - Listar animais")
                    print("5 - Remover animal")
                    print("6 - Atualizar status")
                    print("0 - Sair")

                    escolha = input("Escolha: ").strip()

                    # CADASTRAR ANIMAL
                    if escolha == "3":
                        print("\n--- CADASTRAR ANIMAL ---")
                        tipo = input("Tipo (Bovino, Caprino, Ovino, Suíno): ").strip()
                        identificacao = input("Identificação (brinco/número): ").strip()
                        status = input("Status (lactação, engorda, venda): ").strip()

                        animais.append([tipo, identificacao, status])
                        print("Animal cadastrado com sucesso!")

                    # LISTAR ANIMAIS
                    elif escolha == "4":
                        if not animais:
                            print("0 animais no momento!")
                        else:
                            print("\n--- LISTA DE ANIMAIS ---")
                            for a in animais:
                                print(f"Tipo: {a[0]} | ID: {a[1]} | Status: {a[2]}")

                    # REMOVER ANIMAL
                    elif escolha == "5":
                        print("\n--- REMOVER ANIMAL ---")
                        id_remover = input("Digite o ID do animal: ").strip()

                        animais = [a for a in animais if a[1] != id_remover]

                        print("Remoção concluída!")

                    # ATUALIZAR STATUS
                    elif escolha == "6":
                        print("\n--- ATUALIZAR STATUS ---")
                        id_busca = input("Digite o ID do animal: ").strip()

                        for a in animais:
                            if a[1] == id_busca:
                                novo_status = input("Novo status: ").strip()
                                a[2] = novo_status
                                print("Status atualizado!")
                                break
                        else:
                            print("Animal não encontrado!")

                    elif escolha == "0":
                        print("Saindo do menu ADM...")
                        break

                    else:
                        print("Opção inválida!")

            #================= CLIENTE =================
            elif perfil == "CLIENTE":
                print("BEM VINDO CLIENTE")

                while True:
                    print("\n--- MENU CLIENTE ---")
                    print("4 - Listar animais")
                    print("0 - Sair")

                    escolha = input("Escolha: ").strip()

                    if escolha == "4":
                        if not animais:
                            print("0 animais no momento!")
                        else:
                            print("\n--- LISTA DE ANIMAIS ---")
                            for a in animais:
                                print(f"Tipo: {a[0]} | ID: {a[1]} | Status: {a[2]}")

                    elif escolha == "0":
                        print("Saindo do menu CLIENTE...")
                        break

                    else:
                        print("Opção inválida!")

        else:
            print("Login inválido!")

    # SAIR
    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")