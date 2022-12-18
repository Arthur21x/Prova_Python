from Curso_Udemy.aula75.Prova_Python.colaborador import Colaborador
from Curso_Udemy.aula75.Prova_Python.contratos import Comissionado, Horista, Assalariado, \
    Contrato
from Curso_Udemy.aula75.Prova_Python.Venda import vendasComissionadas


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
                elif classe.cpf == id:
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
        contrato = Assalariado(dia, mes, ano, colaborador, salario, Insalubridade, Periculosidade)
        contrato.ativo = True
        contrato.id = len(lista_contrato) + 1
        print(contrato.id)
        lista_contrato.append(contrato)
    elif op == 2:
        horaMes = int(input("Digite quantas horas você faz por mês: "))
        valorHora = int(input("Digite o valor que você recebe por Hora: "))
        contrato = Horista(dia, mes, ano, colaborador, horaMes, valorHora)
        contrato.ativo = True
        contrato.id = len(lista_contrato) + 1
        lista_contrato.append(contrato)
    elif op == 3:
        comissao = float(input("Digite o seu Percentual de Comissão: "))
        ajudaCusto = float(input("Digite o seu valor de ajuda nos Custos:"))
        contrato = Comissionado(dia, mes, ano, colaborador, comissao, ajudaCusto)
        contrato.ativo = True
        contrato.id = len(lista_contrato) + 1
        lista_contrato.append(contrato)
    return lista_contrato


def consultar_contrato(lista_contrato) -> None:
    print("-" * 40)
    print("Listagem de Contratos")
    print("-" * 40)
    while True:
        id = int(input("Digite o identificador do seu Contrato: "))
        if id in [x for x in range(1, len(lista_contrato) + 1)]:
            break
        print("Digite um ID válido")
    get_contrato = gera_pesquisa(lista_contrato)
    contrato = get_contrato(id)
    print(f"Data do início do Contrato: {contrato.dataInicio}")
    if contrato.dataEncerramento is None:
        print("Data do Encerramento: Não há data de encerramento")
    else:
        print(f"Data do Encerramento: {contrato.dataEncerramento}")
    if contrato.ativo is True:
        print("Situação: Ativo")
    else:
        print("Situação: Desativado")
    print(f"Tipo do Contrato: {contrato.__class__.__name__}")
    print(f"Matrícula do colaborador: {contrato.colaborador.matricula}")
    print(f"Nome do colaborador: {contrato.colaborador.nome}")
    print(f"CPF do colaborador: {contrato.colaborador.cpf}")
    print(f"Situação do colaborador: {contrato.colaborador.situacao}")


def consultar_colaboradores(lista_colaborador) -> None:
    print("-" * 40)
    print("Listagem de Colaboradores Ativos")
    print("-" * 40)
    for colaborador in lista_colaborador:
        if colaborador.situacao is True:
            print(f"Matrícula: {colaborador.matricula}")
            print(f"Nome: {colaborador.nome}")
            print(f"CPF: {colaborador.cpf}")
            print("-" * 40)


def encerrarContrato(lista_contrato):
    print("-" * 40)
    print("Encerramento de Contrato")
    print("-" * 40)
    while True:
        id = int(input("Digite o identificador do seu Contrato: "))
        if id in [x for x in range(1, len(lista_contrato) + 1)]:
            break
        print("Digite um ID válido")
    get_contrato = gera_pesquisa(lista_contrato)
    contrato = get_contrato(id)
    if contrato.ativo is False:
        print("O contrato já está inativo")
        return
    else:
        dia = int(input("Digite o Dia do Encerramento Seu contrato: "))
        mes = int(input("Digite o Mês do Encerramento Seu contrato: "))
        ano = int(input("Digite o ano do Encerramento Seu contrato: "))
        contrato.EncerrarContrato(dia, mes, ano)
        print("-" * 40)
        print(f"Contrato de {contrato.colaborador.nome} foi Encerrado com sucesso")


def consultar_contrato_colaborador(lista_contratos):
    print("-" * 40)
    print("Listagem de contratos")
    print("-" * 40)
    cpf = str(input("Digite o CPF do seu colaborador: "))
    for contrato in lista_contratos:
        if contrato.colaborador.cpf == cpf:
            print("----COLABORADOR----")
            print(f"Nome: {contrato.colaborador.nome}")
            print(f"CPF: {contrato.colaborador.cpf}")
            print(f"Situação: {contrato.colaborador.situacao}")
            print(f"----CONTRATO DE {contrato.colaborador.nome}----")
            print(f"Id: {contrato.id}")
            print(f"Tipo de Contrato: {contrato.__class__.__name__}")
            print(f"Data de início: {contrato.dataInicio}")
            print(f"Data de Encerramento: {contrato.dataEncerramento}")
            print(f"Situação do contrato: {contrato.ativo}")
            break


def lancar_vendas_comissionadas(lista_contratos, venda_comissionada):
    print("-" * 40)
    print("Lançamento de vendas Comissionadas")
    print("-" * 40)
    while True:
        id = int(input("Digite o identificador do seu Contrato: "))
        if id in [x for x in range(1, len(lista_contratos) + 1)]:
            break
        print("Contrato não existe, ou ID inválido, por favor tente novamente!")
    for contrato in lista_contratos:
        tipo_contrato = contrato.__class__.__name__
        if contrato.id == id:
            if tipo_contrato == "Comissionado" and tipo_contrato is True:
                mes = int(input("Digite o Mês das Vendas: "))
                ano = int(input("Digite o ano das Vendas: "))
                valor_total = int(input("Digite o Valor total da vendas do mês: "))
                venda_comissionada.append(vendasComissionadas(mes, ano, valor_total, contrato))
                return venda_comissionada
            elif tipo_contrato != "Comissionado" or contrato.ativo is False:
                print("APENAS CONTRATOS COMISSIONADOS PODEM LANÇAR VENDAS COMISSIONADAS")
                return


def emitir_folha_pagamento(lista_contratos, venda_comissionada):
    print("-" * 40)
    print("Emitir folha de pagamento")
    print("-" * 40)
    while True:
        id = int(input("Digite o identificador do seu Contrato: "))
        if id in [x for x in range(1, len(lista_contratos) + 1)]:
            break
        print("Contrato não existe, ou ID inválido, por favor tente novamente!")
    for contrato in lista_contratos:
        if contrato.ativo is True:
            print("----COLABORADOR----")
            print(f"Nome: {contrato.colaborador.nome}")
            print(f"Matrícula: {contrato.colaborador.matricula}")
            if contrato.__class__.__name__ == "Comissionado":
                for venda in venda_comissionada:
                    if venda.contrComissionado.id == contrato.id:
                        print(f"Salário: {contrato.calcVencimento(venda.valor)}")
            else:
                print(f"Salário: {contrato.calcVencimento()}")
            print(f"----CONTRATO DE {contrato.colaborador.nome}----")
            print(f"Id: {contrato.id}")
            print(f"Tipo de Contrato: {contrato.__class__.__name__}")
        else:
            print("Só é possível emitir folha de contratos ativos")
