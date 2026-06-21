import os
from memoryt import save_clientes
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  
def cadastrar(clientes):
    nome_clt = input("|= Digite o nome do cliente: ")
    print("|=")
    phone_clt = input("|= Digite o telefone do cliente: ")
    print("|=")
    cpf_clt = input("|= Digite o CPF do cliente: ")
    if cpf_clt in clientes or cpf_clt == "":
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==       CPF inválido ou em uso!        ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    else:
        print("|=")
        city_clt = input("|= Digite a cidade do cliente: ")
        clientes[cpf_clt] = [nome_clt, phone_clt, city_clt]
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==   Cliente cadastrado com sucesso!!   ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    input("|= Voltar para o Módulo de clientes <Enter>: ")
    save_clientes(clientes)
    return
def buscar(clientes):
    cpf_clt = input("|= Digite o CPF do cliente: ")
    if cpf_clt in clientes:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==   Cliente encontrado com sucesso!!   ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|=")
        print("|= Nome: ", clientes[cpf_clt][0])
        print("|= Telefone: ", clientes[cpf_clt][1])
        print("|= CPF: ", cpf_clt)
        print("|= Cidade: ", clientes[cpf_clt][2])
        print("|=")
    else:
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        Cliente não encontrado!!      ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    input("|= Voltar para o Módulo de clientes <Enter>: ")
    return
def editar(clientes):
    option3_clt = '' 
    while option3_clt != "0":
        cpf_clt = input("|= Digite o CPF do cliente: ")
        if cpf_clt in clientes:
            while option3_clt != "0":
                limpar_tela()
                print("|==========================================|")
                print("|==")
                print("|== Nome: ", clientes[cpf_clt][0])
                print("|== Telefone: ", clientes[cpf_clt][1])
                print("|== CPF: ", cpf_clt)
                print("|== Cidade: ", clientes[cpf_clt][2])
                print("|==")
                print("|==========================================|")
                print("|============= Editar cliente =============|")
                print("|==========================================|")
                print("|==                                      ==|")
                print("|==        1-Editar nome                 ==|")
                print("|==                                      ==|")
                print("|==        2-Editar telefone             ==|")
                print("|==                                      ==|")
                print("|==        3-Editar CPF                  ==|")
                print("|==                                      ==|")
                print("|==        4-Editar cidade               ==|")
                print("|==                                      ==|")
                print("|==        0-Sair                        ==|")
                print("|==                                      ==|")
                print("|==========================================|")
                print("|==========================================|")
                option3_clt = input("|== Escolha uma opção: ")
                if option3_clt == "1":
                    nome_clt = input("|== Digite o novo nome do cliente: ")
                    clientes[cpf_clt][0] = nome_clt
                    save_clientes(clientes)
                elif option3_clt == "2":
                    phone_clt = input("|== Digite o novo telefone do cliente: ")
                    clientes[cpf_clt][1] = phone_clt
                    save_clientes(clientes)
                elif option3_clt == "3":
                    cpf_antigo = cpf_clt
                    cpf_clt = input("|= Digite o novo CPF do cliente: ")
                    if cpf_clt in clientes:
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==       CPF inválido ou em uso!        ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                        continuar = input("|== Continuar editando [Enter]: ")
                        if continuar.upper() == "N":
                            option3_clt = "0"
                        cpf_clt = cpf_antigo
                    elif cpf_clt == "":
                        print()
                    else:
                        clientes[cpf_clt] = [clientes[cpf_antigo][0], clientes[cpf_antigo][1], clientes[cpf_antigo][2]]
                        del clientes[cpf_antigo]
                        save_clientes(clientes)
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Cliente editado com sucesso!!    ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                elif option3_clt == "4":
                    city_clt = input("|== Digite a nova cidade do cliente: ")
                    clientes[cpf_clt][2] = city_clt
                    save_clientes(clientes)
                    print("|==========================================|")
                    print("|==                                      ==|")
                    print("|==     Cliente editado com sucesso!!    ==|")
                    print("|==                                      ==|")
                    print("|==========================================|")
                elif option3_clt == "0" or option3_clt == "":
                    print()
                else:
                    print("|== Opção inválida!!")
                    if option3_clt != "0":
                        if option3_clt != "":
                            continuar = input("|== Deseja continuar editando? [S/N]: ")
                            if continuar.upper() == "N":
                                option3_clt = "0"
        else:
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==        Cliente não encontrado!!      ==|")
            print("|==                                      ==|")
            print("|==========================================|")
            input("|== Continuar no módulo de clientes <Enter>: ")
            option3_clt = "0"
    return
def remover(clientes):
    cpf_clt = input("|== Digite o CPF do cliente: ")
    if cpf_clt in clientes:
        print("|==")    
        print("|== Nome: ", clientes[cpf_clt][0])
        print("|== Telefone: ", clientes[cpf_clt][1])
        print("|== CPF: ", cpf_clt)
        print("|== Cidade: ", clientes[cpf_clt][2])
        print("|==")
        verificar = input("|== Tem certeza que deseja remover este cliente? (S/N): ")
        if verificar.upper() == "S":
            del clientes[cpf_clt]
            save_clientes(clientes)
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==   Cliente removido com sucesso!!     ==|")
            print("|==                                      ==|")
        print("|==========================================|")
    elif cpf_clt == "":
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==             CPF inválido             ==|")
        print("|==                                      ==|")
        print("|==========================================|")
    input("|== Voltar para o Módulo de clientes <Enter>: ")