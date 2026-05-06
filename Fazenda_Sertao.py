usuarios = [
    ["jonatas", "1234", "ADM"],
    ["jose", "12", "CLIENTE"]
]

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # CADASTRO
    if opcao == "1":
        login = input("Login: ")

        while True:
            senha = input("Senha: ")

            contador = 0
            for letra in senha:
                if letra >= "0" and letra <= "9":
                    contador = contador + 1

            if len(senha) >= 8 and contador >= 2:
                break
            else:
                print("Senha inválida!")

        perfil = input("Perfil (ADM ou CLIENTE): ").upper()

        usuarios.append([login, senha, perfil])
        print("Usuário cadastrado!")

    # LOGIN
    elif opcao == "2":
        login = input("Login: ")
        senha = input("Senha: ")

        usuario = []

        for u in usuarios:
            if u[0] == login and u[1] == senha:
                usuario = u

        if usuario != []:
            print("Login realizado!")

            perfil = usuario[2]

            compra_produtos = []
            quantidade_produtos = []
            data_retiradas = []
            hora_retiradas = []

            while True:
                compra_produtos = input("QUAL PRODUTO VOCE QUER COMPRAR?: ").upper()
                quantidade_produtos = int(input("QUANTIDADE DE PRODUTOS: "))

                # ===== DATA =====
                data_retirada = input("DATA RETIRADA(dd/mm/aaaa): ")

                while len(data_retirada) != 10 or "/" not in data_retirada:
                    print("DATA INVALIDA")
                    data_retirada = input("DIGITE DATA (dd/mm/aaaa): ")

                dataFormatada = data_retirada.split("/")
                dia = dataFormatada[0]
                mes = dataFormatada[1]
                ano = dataFormatada[2]

                while not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                    print("DATA INVALIDA (SO NUMEROS)")
                    data_retirada = input("DATA RETIRADA(dd/mm/aaaa): ")
                    dataFormatada = data_retirada.split("/")
                    dia = dataFormatada[0]
                    mes = dataFormatada[1]
                    ano = dataFormatada[2]

                dia = int(dia)
                mes = int(mes)
                ano = int(ano)

                while ano < 2026:
                    print("ANO INVALIDO")
                    data_retirada = input("DATA RETIRADA(dd/mm/aaaa): ")
                    dataFormatada = data_retirada.split("/")
                    dia = int(dataFormatada[0])
                    mes = int(dataFormatada[1])
                    ano = int(dataFormatada[2])

                while mes < 1 or mes > 12:
                    print("MES INVALIDO")
                    data_retirada = input("DATA RETIRADA(dd/mm/aaaa): ")
                    dataFormatada = data_retirada.split("/")
                    dia = int(dataFormatada[0])
                    mes = int(dataFormatada[1])
                    ano = int(dataFormatada[2])

                while dia < 1 or dia > 31:
                    print("DIA INVALIDO")
                    data_retirada = input("DATA RETIRADA(dd/mm/aaaa): ")
                    dataFormatada = data_retirada.split("/")
                    dia = int(dataFormatada[0])
                    mes = int(dataFormatada[1])
                    ano = int(dataFormatada[2])

                data_retiradas.append(data_retirada)

                # ===== HORA =====
                hora_retirada = input("HORA RETIRADA (hh:mm:ss): ")

                while len(hora_retirada) < 7 or ":" not in hora_retirada:
                    print("HORA INVALIDA")
                    hora_retirada = input("HORA RETIRADA: ")

                horaFormatada = hora_retirada.split(":")
                hora = horaFormatada[0]
                minutos = horaFormatada[1]
                segundos = horaFormatada[2]

                while not (hora.isdigit() and minutos.isdigit() and segundos.isdigit()):
                    print("HORA INVALIDA (SO NUMEROS)")
                    hora_retirada = input("HORA RETIRADA: ")
                    horaFormatada = hora_retirada.split(":")
                    hora = horaFormatada[0]
                    minutos = horaFormatada[1]
                    segundos = horaFormatada[2]

                hora = int(hora)
                minutos = int(minutos)
                segundos = int(segundos)

                while hora < 0 or hora > 23:
                    print("HORA INVALIDA")
                    hora_retirada = input("HORA RETIRADA: ")
                    horaFormatada = hora_retirada.split(":")
                    hora = int(horaFormatada[0])
                    minutos = int(horaFormatada[1])
                    segundos = int(horaFormatada[2])

                while minutos < 0 or minutos > 59:
                    print("MINUTO INVALIDO")
                    hora_retirada = input("HORA RETIRADA: ")
                    horaFormatada = hora_retirada.split(":")
                    hora = int(horaFormatada[0])
                    minutos = int(horaFormatada[1])
                    segundos = int(horaFormatada[2])

                while segundos < 0 or segundos > 59:
                    print("SEGUNDO INVALIDO")
                    hora_retirada = input("HORA RETIRADA: ")
                    horaFormatada = hora_retirada.split(":")
                    hora = int(horaFormatada[0])
                    minutos = int(horaFormatada[1])
                    segundos = int(horaFormatada[2])

                hora_retiradas.append(hora_retirada)

                print(f"Agendamento feito! Produto: {compra_produtos} | Quantidade: {quantidade_produtos}")
                print(f"Data: {data_retirada} | Hora: {hora_retirada}")

                sair = input("Deseja fazer outra compra? (s/n): ")
                if sair != "s":
                    break

        else:
            print("Login inválido!")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")