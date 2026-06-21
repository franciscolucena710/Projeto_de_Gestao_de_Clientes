import os
from memoryt import save_contas
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def cadastrar(contas,clientes):
    cpf_cnt = input("|= Digite o CPF do cliente: ")
    if cpf_cnt in clientes:
        desc_cnt = input("|= Digite a descrição da conta: ")
        valor_cnt = input("|= Digite o valor da conta: ")
        venc_cnt = input("|= Digite a data de vencimento da conta: ")
        contas[cpf_cnt] = [desc_cnt, valor_cnt, venc_cnt]
        save_contas(contas)
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==     Conta adicionada com sucesso!!   ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==")    
        print("|== Nome:",clientes[cpf_cnt][0])
        print("|== CPF:",cpf_cnt)
        print("|== Descrição:",desc_cnt)
        print("|== Débito:",valor_cnt,"R$")
        print("|== Vencimento:",venc_cnt)
    elif cpf_cnt == "":
        print()
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    if cpf_cnt == "":
        print()
    else:
        input("|= Voltar para o Módulo de contas <Enter>: ")
def buscar(contas,clientes):
    cpf_cnt = input("|= Digite o CPF do cliente: ")
    if cpf_cnt in contas:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==   Contas do cliente encontradas!!    ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==")    
        print("|== Nome:",clientes[cpf_cnt][0])
        print("|== CPF:",cpf_cnt)
        print("|== Descrição:",contas[cpf_cnt][0])
        print("|== Débito:",contas[cpf_cnt][1],"R$")
        print("|== Vencimento:",contas[cpf_cnt][2])
        print("|==")
        input("|== Voltar para o Módulo de contas <Enter>: ")
    elif cpf_cnt == "":
        print()
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        input("|== Voltar para o Módulo de contas <Enter>: ")
def editar(contas,clientes):
    option3_cnt = '' 
    while option3_cnt != "0":
        cpf_cnt = input("|= Digite o CPF do cliente: ")
        if cpf_cnt in clientes:
            while option3_cnt != "0":
                limpar_tela()
                print("|==========================================|")
                print("|==")
                print("|== Nome:",clientes[cpf_cnt][0])
                print("|== CPF:",cpf_cnt)
                print("|== Descrição:",contas[cpf_cnt][0])
                print("|== Débito:",contas[cpf_cnt][1],"R$")
                print("|== Vencimento:",contas[cpf_cnt][2])
                print("|==")
                print("|==========================================|")
                print("|=============  Editar conta  =============|")
                print("|==========================================|")
                print("|==                                      ==|")
                print("|==        1-Editar descrição            ==|")
                print("|==                                      ==|")
                print("|==        2-Editar débito               ==|")
                print("|==                                      ==|")
                print("|==        3-Editar cliente              ==|")
                print("|==                                      ==|")
                print("|==        4-Editar vencimento           ==|")
                print("|==                                      ==|")
                print("|==        0-Sair                        ==|")
                print("|==                                      ==|")
                print("|==========================================|")
                print("|==========================================|")
                option3_cnt = input("|== Escolha uma opção: ")
                if option3_cnt == "1":
                    desc_cnt = input("|== Digite a nova descrição da conta: ")
                    contas[cpf_cnt][0] = desc_cnt
                    save_contas(contas)
                    print("|==========================================|")
                    print("|==                                      ==|")
                    print("|==     Conta editada com sucesso!!      ==|")
                    print("|==                                      ==|")
                    print("|==========================================|")
                elif option3_cnt == "2":
                    debito_cnt = input("|== Digite o novo débito da conta: ")
                    contas[cpf_cnt][1] = debito_cnt
                    save_contas(contas)
                    print("|==========================================|")
                    print("|==                                      ==|")
                    print("|==     Conta editada com sucesso!!      ==|")
                    print("|==                                      ==|")
                    print("|==========================================|")
                elif option3_cnt == "3":
                    cpf_antigo = cpf_cnt
                    cpf_cnt = input("|= Digite o CPF do novo dono da conta: ")
                    if cpf_cnt not in clientes:
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==             CPF inválido             ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                        input("|== Continuar editando [Enter]: ")
                        cpf_cnt = cpf_antigo
                    elif cpf_cnt == "":
                        print()
                    else:
                        contas[cpf_cnt] = [contas[cpf_antigo][0], contas[cpf_antigo][1], contas[cpf_antigo][2]]
                        del contas[cpf_antigo]
                        save_contas(contas)
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Conta editada com sucesso!!      ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                elif option3_cnt == "4":
                    vencimento_cnt = input("|== Digite o novo vencimento da conta: ")
                    contas[cpf_cnt][2] = vencimento_cnt
                    save_contas(contas)
                    print("|==========================================|")
                    print("|==                                      ==|")
                    print("|==     Conta editada com sucesso!!      ==|")
                    print("|==                                      ==|")
                    print("|==========================================|")
                elif option3_cnt == "0" or option3_cnt == "":   
                    print()
                else:
                    print("|== Opção inválida!!")
                    if option3_cnt != "0":
                        if option3_cnt != "":
                            continuar = input("|== Deseja continuar editando? [S/N]: ")
                            if continuar.upper() == "N":
                                option3_cnt = "0"
        else:
                print("|==========================================|")
                print("|==                                      ==|")
                print("|==        Cliente não encontrado!!      ==|")
                print("|==                                      ==|")
                print("|==========================================|")
                input("|== Continuar no módulo de clientes <Enter>: ")
                option3_cnt = "0"
def remover(contas,clientes):
    cpf_cnt = input("|= Digite o CPF do cliente: ")
    if cpf_cnt in contas:
        print("|==")    
        print("|== Nome:",clientes[cpf_cnt][0])
        print("|== Descrição: ", contas[cpf_cnt][0])
        print("|== Débito: ", contas[cpf_cnt][1])
        print("|== CPF: ", cpf_cnt)
        print("|== Vencimento: ", contas[cpf_cnt][2])
        print("|==")
        verificar = input("|= Tem certeza que deseja remover esta conta? (S/N): ")
        if verificar.upper() == "S":
            del contas[cpf_cnt]
            save_contas(contas)
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==     Conta removida com sucesso!!     ==|")
            print("|==                                      ==|")
            print("|==========================================|")
    elif cpf_cnt == "":
        print()
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    if cpf_cnt == "" or verificar.upper() != "S":
        print()
    else:
        input("|= Voltar para o Módulo de contas <Enter>: ")