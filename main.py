from modulo.functions import *

lista_colaborador, lista_contratos, lista_vendas_comissionadas = list(), list(), list()
while True:
    comandos = {
        "1": lambda: inserir_Colaborador(lista_colaborador),
        "2": lambda: Registrar_Contrato(lista_colaborador, lista_contratos),
        "3": lambda: consultar_contrato(lista_contratos),
        "4": lambda: encerrarContrato(lista_contratos),
        "5": lambda: consultar_colaboradores(lista_colaborador),
        "6": lambda: consultar_contrato_colaborador(lista_contratos),
        "7": lambda: lancar_vendas_comissionadas(lista_contratos),
        "8": lambda: emitir_folha_pagamento(lista_contratos, lista_vendas_comissionadas)
    }
    menu()
    op = str(input("Digite um valor entre 0 e 8: "))
    if op == 0:
        print("Encerrando o programa.....")
        break
    comando = comandos.get(op)
    comando()
