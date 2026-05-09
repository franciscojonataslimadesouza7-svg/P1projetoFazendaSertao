usuarios = [
    ["12", "12", "ADM"],
    ["jose", "12", "CLI"]
]

rebanho = [
    ["Bovino de Leite", "001", "Em lactação"],
    ["Caprino", "002", "Disponível para venda"]

]

produçao_leite = []

estoque = [
    ["Queijo coalho", 10, 45.0, 70],
    ["Queijo Manteiga", 5, 60.0, 80]
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
                            identificador = input("informe o identificador do animal novo: ")

                            for animal in rebanho:
                                if identificador == animal[1]:
                                    print("Animal encontrado!")
                                    print("tipo:", animal[0])
                                    print("identificado:", animal[1])
                                    print("status:", animal[2])

                                    animal[0] = input("novo tipo do animal: ")
                                    animal[2] = input("novo status do animal: ")

                                    print("animal atualizado com sucesso!!")
                                    break

                        elif op == "4":
                            identificador = input("Informe o identificador do animal: ")

                            for animal in rebanho:
                                if identificador == animal[1]:
                                    rebanho.remove(animal)

                                    print(f"o animal com o identificador {identificador} foi removido com sucesso!!")

                        elif op == "5":
                            litros = input("informe os litros produzidos: ")

                            produçao_leite.append(litros)

                            print(f"{litros} de leite registrado com sucesso!!")

                        elif op == "6":
                            nome_produto = input("Informe o nome do produto: ")
                            peso = input("Informe o peso em kg: ")
                            valor = input("Informe o valor do produto: ")

                            estoque.append([nome_produto, peso, valor])

                            print(f"o {nome_produto} com peso {peso}Kg e valor: R${valor} foi adicionado com sucesso!!")

                        elif op == "7":
                            nome_produto = input("Informe o nome do produto: ")
                            peso = float(input("Informe o peso em kg: "))
                            custo = float(input("Informe o custo do produto: "))
                            preco_venda = float(input("Informe o preço de venda: "))

                            estoque.append([nome_produto, peso, custo, preco_venda])

                            print(f"o {nome_produto} com peso {peso} Kg e custo de R${custo} tem um preço de venda de R${preco_venda}")

                        elif op == "0":
                            print("obrigado por acessar nosso sistema......")
                            break


                    # menu de cliente
                    elif logado[2] == "CLI":
                        print("--- MENU CLIENTE ---")
                        print("1 - Ver estoque")
                        print("2 - Ver rebanho")
                        print("3 - Ver produção de leite")
                        print("0 - Sair")

                        op_cli = input("Escolha a opção: ")

                        if op_cli == "1":
                            for item in estoque and rebanho:
                                print(item)

                        elif op_cli == "2":
                            for animal in rebanho:
                                print(animal)

                        elif op_cli == "3":
                            for litros in produçao_leite:
                                print(litros)

                        elif op_cli == "0":
                            print("Saindo...")
                            break


    elif opcao == "0":
        print("obrigado por acessar nosso sistema......")
        break