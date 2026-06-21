import os
from memoryt import save_pagamentos
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def cadastrar(pagamentos,contas,clientes):
    cpf_pmt = input("|== Digite o CPF da conta: ")
    if cpf_pmt in contas:
        print("|==")    
        print("|== Nome:",clientes[cpf_pmt][0])
        print("|== Descrição: ", contas[cpf_pmt][0])
        print("|== Débito: ", contas[cpf_pmt][1])
        print("|== CPF: ", cpf_pmt)
        print("|== Vencimento: ", contas[cpf_pmt][2])
        print("|==")
        verificar = input("|= Tem certeza que deseja pagar esta conta? (S/N): ")
        if verificar.upper() == "S":
            data_pmt = input("|= Digite a data do pagamento: ")
            quantidade_pmt = len(pagamentos[cpf_pmt]) + 1
            pagamentos[cpf_pmt][quantidade_pmt] = [contas[cpf_pmt][0], contas[cpf_pmt][1], contas[cpf_pmt][2], data_pmt]
            del contas[cpf_pmt]
            save_pagamentos(pagamentos)
        else:
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==         Pagamento cancelado!!        ==|")
            print("|==                                      ==|")
            print("|==========================================|")
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==    Esse cliente não possui contas    ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        input("|= Voltar para o Módulo de pagamentos <Enter>: ")
def buscar(pagamentos,clientes):
    cpf_pmt = input("|== Digite o CPF da conta: ")
    if cpf_pmt in pagamentos:
        limpar_tela()
        print("|==========================================|")
        print("|==                                      ==|")
        print("|== Histórico de pagamentos encontrado!! ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        for pagamento in pagamentos[cpf_pmt].values():
            print("|==")    
            print("|== Nome:",clientes[cpf_pmt][0])
            print("|== Descrição: ", pagamento[0])
            print("|== Débito: ", pagamento[1])
            print("|== CPF: ", cpf_pmt)
            print("|== Vencimento: ", pagamento[2])
            print("|== Data do pagamento: ", pagamento[3])
            print("|==")
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    input("|= Voltar para o Módulo de pagamentos <Enter>: ")
def remover(pagamentos,clientes):
    cpf_pmt = input("|== Digite o CPF da conta: ")
    if cpf_pmt in pagamentos:
        index = 0
        for pagamento in pagamentos[cpf_pmt].values():
            index += 1
            print("|==")
            print("|== Registro:",index)    
            print("|== Nome:",clientes[cpf_pmt][0])
            print("|== Descrição: ", pagamento[0])
            print("|== Débito: ", pagamento[1])
            print("|== CPF: ", cpf_pmt)
            print("|== Vencimento: ", pagamento[2])
            print("|== Data do pagamento: ", pagamento[3])
            print("|==")
        print("|==")
        verificar = input("|== Qual registro quer apagar? [Digite \"0\" para cancelar]: ")
        if verificar.isdigit() and verificar != "0":
            verificar_int = int(verificar)
            del pagamentos[cpf_pmt][verificar_int]
            save_pagamentos(pagamentos)
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==    Registro apagado com sucesso!!    ==|")
            print("|==                                      ==|")
            print("|==========================================|")
            input("|== Voltar para o Módulo de pagamentos <Enter>: ")
        elif verificar == "": 
            print()
        else:
            print("|==")
            print("|== Cancelado")
            print("|==")
            input("|= Voltar <Enter>: ")
    elif cpf_pmt == "":
        print()
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        input("|== Voltar para o Módulo de pagamentos <Enter>: ")
def editar(pagamentos,clientes):
    cpf_pmt = input("|== Digite o CPF da conta: ")
    option4_pmt = ''
    if cpf_pmt in pagamentos:
        while option4_pmt != "0":
            limpar_tela()
            print("|==========================================|")
            print("|==                                      ==|")
            print("|== Histórico de pagamentos encontrado!! ==|")
            print("|==                                      ==|")
            print("|==========================================|")
            index = 0
            for pagamento in pagamentos[cpf_pmt].values():
                index += 1
                print("|==")    
                print("|== Registro:",index)    
                print("|== Nome:",clientes[cpf_pmt][0])
                print("|== Descrição: ", pagamento[0])
                print("|== Débito: ", pagamento[1])
                print("|== CPF: ", cpf_pmt)
                print("|== Vencimento: ", pagamento[2])
                print("|== Data do pagamento: ", pagamento[3])
                print("|==")
            registro_pmt = input("|== Qual registro quer editar? [Digite \"0\" para cancelar]: ")
            if registro_pmt.isdigit() and registro_pmt != "0":
                registro_pmt_int = int(registro_pmt)
                if registro_pmt_int in pagamentos[cpf_pmt]:
                    option4_pmt = ''
                    while option4_pmt != "0":
                        limpar_tela()
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|== Registro de pagamento encontrado!!   ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                        print("|==")    
                        print("|== Nome:",clientes[cpf_pmt][0])
                        print("|== Descrição: ", pagamentos[cpf_pmt][registro_pmt_int][0])
                        print("|== Débito: ", pagamentos[cpf_pmt][registro_pmt_int][1])
                        print("|== CPF: ", cpf_pmt)
                        print("|== Vencimento: ", pagamentos[cpf_pmt][registro_pmt_int][2])
                        print("|== Data do pagamento: ", pagamentos[cpf_pmt][registro_pmt_int][3])
                        print("|==")
                        print("|==========================================|")
                        print("|===========  Editar registro  ============|")
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==        1-Editar descrição            ==|")
                        print("|==                                      ==|")
                        print("|==        2-Editar débito               ==|")
                        print("|==                                      ==|")
                        print("|==        3-Editar vencimento           ==|")
                        print("|==                                      ==|")
                        print("|==        4-Editar data do pagamento    ==|")
                        print("|==                                      ==|")
                        print("|==        0-Sair                        ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                        print("|==========================================|")
                        option4_pmt = input("|== Escolha uma opção: ")    
                        if option4_pmt == "1":
                            desc_pmt = input("|== Digite a nova descrição do pagamento: ")
                            pagamentos[cpf_pmt][registro_pmt_int][0] = desc_pmt
                            save_pagamentos(pagamentos)
                            print("|==========================================|")
                            print("|==                                      ==|")
                            print("|==     Pagamento editado com sucesso!!  ==|")
                            print("|==                                      ==|")
                            print("|==========================================|")
                        elif option4_pmt == "2":
                            debito_pmt = input("|== Digite o novo débito do pagamento: ")
                            pagamentos[cpf_pmt][registro_pmt_int][1] = debito_pmt
                            save_pagamentos(pagamentos)
                            print("|==========================================|")
                            print("|==                                      ==|")
                            print("|==     Pagamento editado com sucesso!!  ==|")
                            print("|==                                      ==|")
                            print("|==========================================|")
                        elif option4_pmt == "3":
                            vencimento_pmt = input("|== Digite o novo vencimento do pagamento: ")
                            pagamentos[cpf_pmt][registro_pmt_int][2] = vencimento_pmt
                            save_pagamentos(pagamentos)
                            print("|==========================================|")
                            print("|==                                      ==|")
                            print("|==     Pagamento editado com sucesso!!  ==|")
                            print("|==                                      ==|")
                            print("|==========================================|")
                        elif option4_pmt == "4":
                            data_pmt = input("|== Digite a nova data do pagamento: ")
                            pagamentos[cpf_pmt][registro_pmt_int][3] = data_pmt
                            save_pagamentos(pagamentos)
                            print("|==========================================|")
                            print("|==                                      ==|")
                            print("|==     Pagamento editado com sucesso!!  ==|")
                            print("|==                                      ==|")
                            print("|==========================================|") 
                        elif option4_pmt == "0":
                            option4_pmt = "0"
                        else:
                            print("|== Opção inválida!!")
                        if option4_pmt != "0":
                            if option4_pmt != "":
                                continuar = input("|== Deseja continuar editando? [S/N]: ")
                                if continuar.upper() == "N":
                                    option4_pmt = "0"
                elif registro_pmt == "0":
                    print("|==")
                    print("|== Cancelado")
                    print("|==")
                    input("|== Voltar <Enter>: ")
                    option4_pmt = "0"                      
                else:
                    print()
