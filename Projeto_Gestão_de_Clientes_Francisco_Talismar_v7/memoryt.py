import ast
def save_clientes(clientes):
    arq = open('clientes.txt', 'w', encoding='utf-8')
    for cliente in clientes:
        arq.write(cliente + '\n')
        for info in clientes[cliente]:
            arq.write(info + '\n')
    arq.close()
def save_contas(contas):
    arq2 = open('contas.txt', 'w', encoding='utf-8')
    for conta in contas:
        arq2.write(conta + '\n')
        for info in contas[conta]:
            arq2.write(info + '\n')
    arq2.close()
def save_pagamentos(pagamentos):
    arq3 = open('pagamentos.txt', 'w', encoding='utf-8')
    arq3.write(str(pagamentos))
    arq3.close()

# Função para carregar os dados dos arquivos #
def load():
    try:
        clientes = {}
        arq = open('clientes.txt', 'r', encoding='utf-8')
        linhas = []
        for linha in arq:
            linhas.append(linha.rstrip())
        arq.close()
        for i in range(0, len(linhas), 4):
            id_cliente = linhas[i]
            nome = linhas[i+1]
            telefone = linhas[i+2]
            cidade = linhas[i+3]
            clientes[id_cliente] = [nome, telefone, cidade]
        contas = {}
        arq2 = open('contas.txt', 'r', encoding='utf-8')
        linhas2 = []
        for linha in arq2:
            linhas2.append(linha.rstrip())
        arq2.close()
        for i in range(0, len(linhas2), 4):
            id_cliente = linhas2[i]
            desc = linhas2[i+1]
            valor = linhas2[i+2]
            vencimento = linhas2[i+3]
            contas[id_cliente] = [desc, valor, vencimento]
        arq3 = open('pagamentos.txt', 'r', encoding='utf-8')
        conteudo_do_arquivo = arq3.read()
        arq3.close()
        pagamentos = ast.literal_eval(conteudo_do_arquivo)
    except:
        clientes = { "1": ["João Silva", "123456789", "São Paulo"], 
             "2": ["Maria Santos", "987654321", "Rio de Janeiro"],
             "3": ["Pedro Oliveira", "456789123", "Belo Horizonte"] }
        contas = { "1": ["Batatas", "10.00", "12-06-2026"],
           "2": ["Arroz", "20.00", "07-07-2026"],
           "3": ["Feijão", "15.00", "10-08-2026"]}
        pagamentos = { "1": {1: ["Batatas", "10.00", "12-06-2026", "12-05-2026"],
                     2: ["Batatas doce", "20.00", "07-07-2028", "07-06-2026"]},
               "2": {1: ["Arroz", "20.00", "07-07-2026", "07-06-2026"],
                     2: ["Arroz integral", "30.00", "10-08-2026", "10-07-2026"]}}
    return clientes, contas, pagamentos