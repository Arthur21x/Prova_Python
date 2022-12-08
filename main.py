from colaborador import Colaborador
from contratos import ContratoComissionado, ContratoHorista, ContratoAssalariado, Contrato
from Venda import vendasComissionadas


def menu():
    print("-" * 40)
    itens = ["Encerrar Programa", "Inserir Colaborador", "Registrar Contrato", "Consultar Contrato",
             "Encerrar contrato", "Listar Colaboradores ativos", "Consultar contratos do Colaborador",
             "Lançar Venda Comissionada", "Emitir Folha de Pagamento"]
    for index, item in enumerate(itens):
        print(f"{index} - {item}")
    print("-" * 40)


def inserir_Colaborador(lista_colaboradores) -> list:
    print("-" * 40)
    print("\t\tInserção de Colaborador")
    print("-" * 40)
    while True:
        matricula = str(input("Digite a sua matrícula:"))
        if matricula.isnumeric():
            break
    cpf = str(input("Digite o seu CPF:"))
    nome = str(input("Digite o seu Nome Completo:"))
    dia = int(input("Digite o Dia em que Nasceu:"))
    mes = int(input("Digite o Mês em que Nasceu:"))
    ano = int(input("Digite o ano em que Nasceu:"))
    colaborador = Colaborador(matricula, cpf, nome, dia, mes, ano)
    if colaborador.valida_cpf():
        lista_colaboradores.insert(len(lista_colaboradores), colaborador)
        print("-" * 40)
        print(f"Colaborador {colaborador.nome} criado com Sucesso")
        return lista_colaboradores
    raise ValueError("O CPF digitado não é válido")


def gera_pesquisa(lista_classe):
    def pesquisa_classe(id):
        for classe in lista_classe:
            try:
                if classe.id == id:
                    return classe
            except AttributeError:
                if classe.matricula == id:
                    return classe

    return pesquisa_classe


def Registrar_Contrato(lista_colaborador, lista_contrato) -> list:
    matricula = str(input("Digite a Matricula do colaborador: "))
    get_colaborador = gera_pesquisa(lista_colaborador)
    colaborador = get_colaborador(matricula)
    colaborador.ativar()
    contratos = [
        "Contrato Assalariado",
        "Contrato Horista",
        "Contrato Comissionado"
    ]
    for index, contrato in enumerate(contratos):
        print(f"\t{index + 1} - {contrato}")
    print("-" * 40)
    while True:
        op = int(input("\tDigite o tipo do Seu Contrato: "))
        if op in [1, 2, 3]:
            break
    print("-" * 40)
    dia = int(input("Digite o Dia do Seu contrato: "))
    mes = int(input("Digite o Mês do Seu contrato: "))
    ano = int(input("Digite o ano do Seu contrato: "))
    if op == 1:
        salario = float(input("Digite o seu salário: "))
        Insalubridade = float(input("Digite o percentual de Insalubridade: "))
        Periculosidade = float(input("Digite o percentual de Periculosidade: "))
        contrato = ContratoAssalariado(dia, mes, ano, colaborador, salario, Insalubridade, Periculosidade)
        contrato.ativo = True
        lista_contrato.append(contrato)
    elif op == 2:
        horaMes = int(input("Digite quantas horas você faz por mês: "))
        valorHora = int(input("Digite o valor que você recebe por Hora: "))
        contrato = ContratoHorista(dia, mes, ano, colaborador, horaMes, valorHora)
        contrato.ativo = True
        lista_contrato.append(contrato)
    elif op == 3:
        comissao = float(input("Digite o seu Percentual de Comissão: "))
        ajudaCusto = float(input("Digite o seu valor de ajuda nos Custos:"))
        contrato = ContratoComissionado(dia, mes, ano, colaborador, comissao, ajudaCusto)
        contrato.ativo = True
        lista_contrato.append(contrato)
    return lista_contrato


def consultar_contrato(lista_contrato) -> None:
    print("-" * 40)
    print("Listagem de Colaboradores Ativos")
    print("-" * 40)
    id = str(input("Digite o identificador do seu Contrato: "))
    get_contrato = gera_pesquisa(lista_contrato)
    contrato = get_contrato(id)
    contrato = contrato.__dict__
    for k, v in contrato.items():
        print(f"{k}: {v}")
    print("-"*40)


def consultar_colaboradores(lista_colaborador) -> None:
    print("-" * 40)
    print("Listagem de Colaboradores Ativos")
    print("-" * 40)
    for colaborador in lista_colaborador:
        if colaborador.situacao is True:
            print(f"Matrícula: {colaborador.matricula}")
            print(f"Nome: {colaborador.nome}")
            print(f"CPF: {colaborador.cpf}")
            print("-"*40)


lista_colaborador, lista_contratos = list(), list()
while True:
    comandos = {
        "1": lambda: inserir_Colaborador(lista_colaborador),
        "2": lambda: Registrar_Contrato(lista_colaborador, lista_contratos),
        "3": lambda: consultar_contrato(lista_contratos),
        "5": lambda: consultar_colaboradores(lista_colaborador)
    }
    menu()
    op = str(input("Digite um valor entre 0 e 8: "))
    if op == 0:
        break
    comando = comandos.get(op)
    comando()
