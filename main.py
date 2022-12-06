from colaborador import Colaborador
from contratos import ContratoComissionado, ContratoHorista, ContratoAssalariado
from Venda import vendasComissionadas


def menu():
    print("-" * 40)
    itens = ["Encerrar Programa", "Inserir Colaborador", "Registrar Contrato", "Consultar Contrato",
             "Encerrar contrato", "Listar Colaboradores ativos", "Consultar contratos do Colaborador",
             "Lançar Venda Comissionada", "Emitir Folha de Pagamento"]
    for index, item in enumerate(itens):
        print(f"{index} - {item}")
    print("-" * 40)


def Inserir_Colaborador(lista_colaborador) -> list:
    while True:
        matricula = str(input("Digite a sua matrícula:"))
        if matricula.isnumeric():
            break
    cpf = str(input("Digite o seu CPF:"))
    nome = str(input("Digite o seu Nome Completo:"))
    dia = int(input("Digite o Dia em que Nasceu:"))
    mes = int(input("Digite o Mês em que Nasceu:"))
    ano = int(input("Digite o ano em que Nasceu:"))
    print("-" * 40)
    colaborador = Colaborador(matricula, cpf, nome, dia, mes, ano)
    if colaborador.valida_cpf():
        lista_colaborador.append(colaborador)
        return lista_colaborador
    raise ValueError("O CPF digitado não é válido")


def Pesquisar_colaborador(matricula, lista_colaborador) -> Colaborador:
    for colaborador in lista_colaborador:
        if colaborador.matricula == matricula:
            return colaborador


def Registrar_Contrato(lista_colaborador, lista_contrato) -> list:
    matricula = str(input("Digite a Matricula do colaborador: "))
    colaborador = Pesquisar_colaborador(matricula, lista_colaborador)
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
        Insalubridade = float(input("Digite o percentual de Insalubridade"))
        Periculosidade = float(input("Digite o percentual de Periculosidade"))
        contrato = ContratoAssalariado(dia, mes, ano, colaborador, salario, Insalubridade, Periculosidade)
        contrato.ativo = True
        lista_contrato.append(contrato)
        return lista_contrato
    elif op == 2:
        horaMes = int(input("Digite quantas horas você faz por mês: "))
        valorHora = int(input("Digite o valor que você recebe por Hora: "))
        contrato = ContratoHorista(dia, mes, ano, colaborador, horaMes, valorHora)
        contrato.ativo = True
        lista_contrato.append(contrato)
        return lista_contrato
    elif op == 3:
        comissao = float(input("Digite o seu Percentual de Comissão: "))
        ajudaCusto = float(input("Digite o seu valor de ajuda nos Custos:"))
        contrato = ContratoComissionado(dia, mes, ano, colaborador, comissao, ajudaCusto)
        contrato.ativo = True
        lista_contrato.append(contrato)
        return lista_contrato


lista_colaborador, lista_contratos = list, list
while True:
    comandos = {
        "1": lambda: Inserir_Colaborador(lista_colaborador),
        "2": lambda: Registrar_Contrato(lista_colaborador, lista_contratos)
    }
    menu()
    op = str(input("Digite um valor entre 0 e 8: "))
    if op == 0:
        break
    comando = comandos.get(op)
    comando()
