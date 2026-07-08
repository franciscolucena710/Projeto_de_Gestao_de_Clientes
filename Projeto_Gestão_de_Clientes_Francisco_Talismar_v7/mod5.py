from datetime import datetime
def relatorio_geral(clientes,contas,pagamentos):
    for cliente in clientes:
        print("|==========================================|")
        print("|== cliente: ", clientes[cliente][0])
        print("|== cpf: ", cliente)
        print("|== telefone: ", clientes[cliente][1])
        print("|== cidade: ", clientes[cliente][2])
        if cliente in contas:
            print("|== Possui conta: Sim")
            print("|== Descrição da conta: ", contas[cliente][0])
            print("|== Valor da conta: ", contas[cliente][1])
            print("|== Data de vencimento: ", contas[cliente][2])
        else:
            print("|== Possui conta: Não")
        if cliente in pagamentos:
            print("|== Possui pagamentos: Sim")
            print("|== (Acesse o módulo de Pagamentos)")
        else:
            print("|== Possui pagamentos: Não")   
    print("|==========================================|")
    input("Pressione Enter para continuar...")

def relatorio_cidade(clientes,contas,pagamentos):
    cidade = input("Digite a cidade para gerar o relatório: ")
    contador = 0
    for cliente in clientes:
        if clientes[cliente][2].lower() == cidade.lower():
            contador += 1
            print("|==========================================|")
            print("|== cliente: ", clientes[cliente][0])
            print("|== cpf: ", cliente)
            print("|== telefone: ", clientes[cliente][1])
            print("|== cidade: ", clientes[cliente][2])
            if cliente in contas:
                print("|== Possui conta: Sim")
                print("|== Descrição da conta: ", contas[cliente][0])
                print("|== Valor da conta: ", contas[cliente][1])
                print("|== Data de vencimento: ", contas[cliente][2])
            else:
                print("|== Possui conta: Não")
            if cliente in pagamentos:
                print("|== Possui pagamentos: Sim")
                print("|== (Acesse o módulo de Pagamentos)")
            else:
                print("|== Possui pagamentos: Não")
    if contador == 0:
        print("|==========================================|")
        print("|==      Nenhum cliente encontrado       ==|")       
    print("|==========================================|")
    input("Pressione Enter para continuar...")

def relatorio_vencimentos(clientes,contas,pagamentos):
    for conta in contas:
        data_conta = contas[conta][2]
        venc_conta = datetime.strptime(data_conta, "%d-%m-%Y").date()
        dia_atual = datetime.now().date()
        soma = 0
        if venc_conta < dia_atual:
            dif = (dia_atual - venc_conta).days
            soma += 1
            print("|==========================================|")
            print("|== cliente: ", clientes[conta][0])
            print("|== cpf: ", conta)
            print("|== telefone: ", clientes[conta][1])
            print("|== cidade: ", clientes[conta][2])
            print("|== Possui conta: Sim")
            if conta in contas:
                print("|== Descrição da conta: ", contas[conta][0])
                print("|== Valor da conta: ", contas[conta][1])
                print("|== Data de vencimento: ", contas[conta][2])
            else:
                print("|== Possui conta: Não")
            if conta in pagamentos:
                print("|== Possui pagamentos: Sim")
                print("|== (Acesse o módulo de Pagamentos)")
            else:
                print("|== Possui pagamentos: Não")
            print("|== Dias atrasados: ", dif,"!!")
    print("|==========================================|")
    if soma == 0:
        print("|==      Nenhum cliente encontrado       ==|")
        print("|==        com contas vencidas!!         ==|")
    else:
        print("|==      Total de clientes com")
        print("|==        contas vencidas:", soma)
    print("|==========================================|")
    input("Pressione Enter para continuar...")

def relatorio_especifico(clientes):
    type_data = input("Digite o tipo de dado para filtrar (cpf, nome, telefone, cidade): ")
    if type_data.lower() == "cpf":
        for cliente in clientes:
            print("|==========================================|")
            print("|== cpf: ", cliente)
    elif type_data.lower() == "nome":
        for cliente in clientes:
            print("|==========================================|")
            print("|== cliente: ", clientes[cliente][0])
    elif type_data.lower() == "telefone":
        for cliente in clientes:
            print("|==========================================|")
            print("|== telefone: ", clientes[cliente][1])
    elif type_data.lower() == "cidade":
        for cliente in clientes:
            print("|==========================================|")
            print("|== cidade: ", clientes[cliente][2])
    else:
        print("|==========================================|")
        print("|==           Opção inválida!!           ==|")
    print("|==========================================|")
    input("Pressione Enter para continuar...")
    