import re  # Importa o módulo 're' para validação do formato de email

# Função para exibir o menu do Salesforce
def getMenu():
    print("====MENU SALESFORCE=====")
    print("1. Cadastro")
    print("2. Login")
    print("3. Logout")  
    print("4. Visualizar Cadastros")
    print("5. Chat de voz")
    print("6. Sair")

# Função para realizar o cadastro de um usuário
def Cadastro(listaDeUsuarios):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    if not idade.isnumeric():
        print("Idade deve ser um número inteiro.")
        return listaDeUsuarios

    email = input("Digite seu email: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Email não é válido.")
        return listaDeUsuarios

    senha = input("Digite sua senha: ")

    if len(senha) < 8:
        print("Senha deve ter pelo menos 8 caracteres.")
        return listaDeUsuarios

    sexo = input("Digite seu sexo: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha,
        "sexo": sexo,
    }

    listaDeUsuarios.append(usuario)
    print("Cadastro realizado com sucesso.")
    return listaDeUsuarios

# Função para realizar o login de um usuário
def Login(listaDeUsuarios, isUsuarioOnline):
    emailLogin = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for usuario in listaDeUsuarios:
        if usuario["email"] == emailLogin and usuario["senha"] == senha:
            isUsuarioOnline = True
            print("Login bem-sucedido.")
            return isUsuarioOnline

    print("Login falhou. Usuário não encontrado ou senha incorreta.")
    return isUsuarioOnline

# Função para realizar o logout
def Logout(isUsuarioOnline):
    if isUsuarioOnline:
        isUsuarioOnline = False
        print("Logout bem-sucedido.")
    else:
        print("Nenhum usuário logado para realizar logout.")
    return isUsuarioOnline

# Função para visualizar os cadastros existentes
def VisualizarCadastros(listaDeUsuarios):
    if not listaDeUsuarios:
        print("Nenhum cadastro realizado.")
    else:
        print("Cadastros existentes:")
        for idx, usuario in enumerate(listaDeUsuarios, 1):
            print(f"Usuário {idx}:")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Email: {usuario['email']}")
            print(f"Sexo: {usuario['sexo']}")
            print()

# Função para iniciar um chat de voz
def chatzin():
    print("Iniciando chat de voz...")

if __name__ == "__main__":
    vmenu = 1
    isUsuarioOnline = False
    listaDeUsuarios = []

    while vmenu == 1:
        getMenu()
        resposta = input("Selecione uma opção: ")

        if resposta == '1':
            listaDeUsuarios = Cadastro(listaDeUsuarios)
        elif resposta == '2':
            if isUsuarioOnline:
                print("Usuário já logado.")
            else:
                isUsuarioOnline = Login(listaDeUsuarios, isUsuarioOnline)
        elif resposta == '3':
            isUsuarioOnline = Logout(isUsuarioOnline)  # Adicionada a opção de Logout
        elif resposta == '4':
            VisualizarCadastros(listaDeUsuarios)  # opção para visualizar cadastros
        elif resposta == '5':
            chatzin()
        elif resposta == '6':
            vmenu = 0
            print("Saindo do programa.")
        else:
            print("Opção inválida! Digite um valor válido.")

    print("Execução encerrada! Volte sempre!")
