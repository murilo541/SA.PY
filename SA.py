pessoas = []
senhas = []
salas = ["Sala do menino mal", "Sala de Reuniao 2", "Auditorio"]
reservas = []
salas_reservadas = []


def selecionar_p():
    global reservas
    a = int(input(f"Digite o numero da pessoa que deseja conversar com o menino mal  {len(pessoas)} ):  "))

    #reservas.insert(pessoas[a-1])
    return pessoas[a-1]





    






    



def selecionar_sala():
    while True:
        sala_selecionada = input(f"selecione uma sala.\nsalas: {salas}")
        for i in salas:
            if sala_selecionada.lower() == i.lower():
                return sala_selecionada
    
def selecionar_data():
    data_valida = False
    while not data_valida:
        data = input("digite a data desejada para a reserva (dd/mm/aaaa): ")
        data_valida = validar_data(data)
    return data

def selecionar_horario():
    horario_valido = False
    while not horario_valido:
        hora = input("digite o horario que deseja reservar (formato => hh:mn ex: 13:30)")
        horario_valido = validar_horario(hora)
    return hora

def validar_horario(horario):
    horario.strip()
    horario = horario.split(":")
    if len(horario) > 2:
        return False
    for i in horario:
        if not i.isnumeric():
            return False 
    if int(horario[0]) > 24:
        return False 
    if int(horario[1]) > 59:
        return False 
    return True

def validar_data(data):
    data.strip()
    data = data.split("/")
    dia = int(data[0])
    mes = int(data[1])
    if mes in  [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    if mes in [4, 6, 9, 11]:
        return dia <= 30
    if mes == 2:
        return dia <= 28
    else:
        print("digite uma data válida!")
        return False

def agenda(sala_s = None):
    global reservas
    while True:
        pessoa = selecionar_p()
        reserva = dict()
        reserva["nome"] = pessoa["nome"]
        if sala_s == None:
            sala = selecionar_sala()
            reserva["sala"] = sala

        if sala_s != salas[0]:
            return 
        else:
            reserva["sala"] = sala_s

      
        data = selecionar_data()
        reserva["data"] = data
        hora = selecionar_horario()
        reserva["horario"] = hora

        deuBoa = True
        for sala_reservada in reservas:
            if sala_reservada["sala"] == reserva["sala"] and sala_reservada["data"] == reserva["data"] and sala_reservada["horario"] == reserva["horario"]:
                print("essa sala ja esta reservada nesta data e nesse horario!")
                deuBoa = False
                break
        
        if deuBoa:
            reservas.append(reserva)
            print(reservas)

        
        

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    if cpf == cpf[0] * 11:
        return False

    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = (soma1 * 10) % 11
    digito1 = 0 if resto1 == 10 else resto1

    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    resto2 = (soma2 * 10) % 11
    digito2 = 0 if resto2 == 10 else resto2

    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def validar_email(email):
    valido = 0
    for i in email:
        if i == "@":
            valido += 1
    testando = email.split("@")
    for i in testando[1]:
        if i == ".":
            valido += 1 
    for i in testando[1]:
        if len(email) < 8:
            valido += 1
        if valido == 3:
             print("email cadastrado com sucesso!")
        return email
    else:
        print("o email nao é valido!")
        

def validar_idade():
    while True:
        idade = input("qual é sua idade? \n")
        if idade.strip():
            valido = 0
            for i in idade:
                if i.isnumeric():
                    valido += 1
        if valido == len(idade):
            idade = int(idade)
            if idade > 0 and idade >= 18:
                return idade
        else: print("a idade não é valida!")
  
def nome(): 
    while True:
        nome = input("\ndigite o seu nome por favor: ")
        if nome.strip():
            nome2 = nome.split(" ")
            for i in nome2:
                for x in i:
                    if x.isnumeric():
                        aprovado = False 
                    else: aprovado = True 
            if aprovado == True:
                return nome
        else : print("o nome é invalido, digite-o novamente!: ")    

def cep():
    while True:
        cep = input("digite o seu cep por favor: ")
        if cep.strip():
            cep = cep.replace(".", "")
            cep = cep.replace("-", "")
            valido = 0
            for i in cep:
                if i.isnumeric():
                    i = int(i)
                    valido += 1
        if len(cep) == 8:
            if valido == len(cep):
                return cep

def cadastrar_p():
    global pessoas
    nome_individuo = nome()
    idade_individuo = validar_idade()
    cpf = pedir_cpf()
    email_individuo = pedir_email()
    cep_individuo = cep()
    senha = input("digite uma senha de acesso: ")
    pessoa = {
        "nome" : nome_individuo,
        "idade" : idade_individuo,
        "CPF" : cpf,
        "email" : email_individuo,
        "cep" : cep_individuo
    }

    pessoas.append(pessoa)
    return pessoa

def mostrar_dicionario(d):
    for chave, valor in d.items():
        print(f"{chave.capitalize():<10}: {valor}")

def listar():
    for i, pessoa in enumerate(pessoas, 1):
        print(f"\n--- Usuário {i} ---")
        mostrar_dicionario(pessoa)

def menu():
    print("Professores Cadatrados: ")
    while True:
        print("--------ESCOLHA SUA OPÇAO--------")
        print("1- CADASTRAR PROFESSOR(A)")
        print("2- LISTAR PROFESSORES")
        print("3- ALTERAR INFORMAÇÕES 🔒️")
        print("4- DELETAR UM USUARIO 🔒️")
        print("5- marcar conversinha com o menino mal")
        print("6- SAIR DO SISTEMA")
        opcao = input("Digite a opçao que voce deseja: ")
        
        if opcao == 1:
            cadastrar_p()
        if opcao == 2:
            listar()
        if opcao == 5:
            agenda(salas[0])    
            


def pedir_cpf():
    cpf_valido = False 
    while not cpf_valido:
        cpf = input("digite seu cpf: ")
        cpf_valido = validar_cpf(cpf)
    return cpf   

def pedir_email():
    email_valido = False 
    while not email_valido:
        email = input("digite seu email: ")
        email_valido = validar_email(email)
    return email

menu()