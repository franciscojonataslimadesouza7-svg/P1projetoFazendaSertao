# LOGIN
while login == usuarios[0][1]:
    print("bem vindo ADM")

while login == usuarios[2][3]:
    print("bem vindo CLIENTE")

if opcao == "1":
    while True:
        login = input("Login: ")
        senha = input("Senha: ")
        credencial = input("Credencial (ADM ou CLIENTE): ")
        usuarios.append([login, senha, credencial])

        print("Usuário cadastrado com sucesso!")
        break





