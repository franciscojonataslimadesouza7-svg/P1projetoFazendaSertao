# usuarios = [
#     ["jonatas", "123", "ADM"],
#     ["maria", "abc", "CLIENTE"]
# ]
#
# animais = []
#
# while True:
#     print("\n-------- MENU --------")
#     print("1 - Cadastrar usuário")
#     print("2 - Listar usuários")
#     print("3 - Login")
#     print("0 - Sair")
#
#     opcao = input("Escolha: ")
#
#     # CADASTRAR USUÁRIO
#     if opcao == "1":
#         login = input("Login: ")
#         senha = input("Senha: ")
#         perfil = input("Perfil (ADM/CLIENTE): ")
#
#         usuarios.append([login, senha, perfil])
#         print("Usuário cadastrado!")
#
#     # LISTAR USUÁRIOS
#     elif opcao == "2":
#         for u in usuarios:
#             print(u[0], "-", u[2])
#
#     # LOGIN
#     elif opcao == "3":
#         print("\n--- LOGIN ---")
#         login = input("Login: ")
#         senha = input("Senha: ")
#
#         usuario = []
#
#         for u in usuarios:
#             if u[0] == login and u[1] == senha:
#                 usuario = u
#
#         if usuario != []:
#             print("Login realizado!")
#
#             perfil = usuario[2]


   # R6

compra_produtos = []
uantidade_produtos = []
data_retiradas = []
hora_retiradas = []

while True:
 compra_produtos = input("QUAL PRODUTO VOCE QUER COMPRAR?: ").upper()
 quantidade_produtos = int(input("QUANTIDADE DE PRODUTOS: "))

 data_retirada = input("DATA RETIRADA(aa/aa/aa): ")
 while len(data_retirada) != 10 or "/" not in data_retirada :
     print("DATA INVALIDA")
     data_retirada = input(" DIGITE DATA (aa/aa/aa): ")

 dataFormatada = data_retirada.split("/")
 dia = dataFormatada[0]
 mes = dataFormatada[1]
 ano = int(dataFormatada[2])

 while ano < 2026:
      print("ANO INVALIDO (PRECISA SER 2026 OU MAIOR)")
      data_retirada = input("DATA RETIRADA(aa/aa/aa): ")

 while mes > 3:
     print("MES INVALIDO(PRECISA SER 2 DIGITOS)")
     data_retirada = input("DATA RETIRADA(aa/aa/aa): ")

 while dia > 3:
     print("DIA INVALIDO(PRECISA SER 2 DIGITOS)")
     data_retirada = input("DATA RETIRADA(aa/aa/aa): ")


 hora_retirada = input("HORA RETIRADA: ")

 while len(hora_retirada) == 10 or ":" not in hora_retirada:
     print("HORA INVALIDA")
     hora_retirada = input("HORA RETIRADA: ")

 horaFormatada = hora_retirada.split(":")
 hora = horaFormatada[0]
 minutos = horaFormatada[1]
 segundos = horaFormatada[2]


 print(f"agendamento feito com sucesso voce vai pegar {quantidade_produtos} | {compra_produtos}  no dia {dia} | do mes {mes} | as {hora_retirada}.")
 break


