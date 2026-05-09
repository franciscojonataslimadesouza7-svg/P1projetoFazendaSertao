usuarios = [
    ["12", "12", "ADM"],
    ["jose", "12", "CLI"]
]

rebanho = [
    ["Bovino de Leite", "001", "Em lactação"],
    ["Caprino", "002", "Disponível para venda"]
]

while True:
    print("\n--- MENU ---")
    print("1 - Login")
    print("0 - Sair")

    opcao = input("Escolha (1 - Login, 0 - Sair): ")

    # LOGIN
    if opcao == "1":

        while True:
            login = input("Login: ")
            senha = input("Senha: ")
            logado =  " "

            for user in usuarios:
                if login == user[0] and senha == user[1]:
                    logado = user

            if logado:
                while True:
                    if logado[2] == "ADM":
                        print("\n--- MENU ADM ---")
                        print("1 - Cadastrar animais")
                        print("2 - Buscar animais")
                        print("3 - Atualizar animais")
                        print("4 - Remover animais")
                        print("5 - Registrar produção de leite")
                        print("6 - Adicionar produtos ao estoque")
                        print("7 - Definir preço de venda")
                        print("0 - Sair")
                        op = input("Escolha a opção: ")

                        if op == "1":
                            tipo_animal = input("Informe o tipo do animal: ")
                            identificador = input("Informe o identificador do animal: ")
                            status = input("Informe o status do animal: ")

                            rebanho.append([tipo_animal, identificador, status])

                            print(f"Animal {tipo_animal} cadastrado com sucesso!")

                        elif op == "2":
                            identificador = input("Informe o identificador do animal: ")

                            for animal in rebanho:

                                if identificador == animal[1]:
                                    print("Animal encontrado!")
                                    print("tipo:", animal[0])
                                    print("identificado:", animal[1])
                                    print("status:", animal[2])


                        elif op == "3":
                            tipo_animal = input("Informe o tipo do animal: ")
                            identificador = input("Informe o identificador do animal: ")
                            status = input("Informe o status do animal: ")

                            rebanho.append([tipo_animal, identificador, status])
                            print("animal atualizado com sucesso!!")



                        elif op == "3":
                          identificador = input("Informe o identificador do animal: ")

                          for animal in rebanho:
                              if identificador == aniaml[1]
                                  rebanho.remove(animal)

                                    print("animal removido com sucesso")




                    elif logado[2] == "CLI":
                        input("\n-----MENU-----")
                        print()

    elif opcao == "0":
        print("obrigado por acessar nosso sistema......")
        break