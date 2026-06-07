import os
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clientes = { "1": ["João Silva", "123456789", "São Paulo"], 
             "2": ["Maria Santos", "987654321", "Rio de Janeiro"],
             "3": ["Pedro Oliveira", "456789123", "Belo Horizonte"] }
contas = { "1": ["Batatas", "10.00", "12-06-2026"],
           "2": ["Arroz", "20.00", "07-07-2026"],
           "3": ["Feijão", "15.00", "10-08-2026"]}
option = ''
while option != "0":
  limpar_tela()
  print("|==========================================|")
  print("|=========== Gestão de clientes ===========|")
  print("|==========================================|")
  print("|==                                      ==|")
  print("|==        1-Módulo Clientes             ==|")
  print("|==                                      ==|")
  print("|==        2-Módulo Contas               ==|")
  print("|==                                      ==|")
  print("|==        3-Módulo Pagamentos           ==|")
  print("|==                                      ==|")
  print("|==        4-Módulo de informações       ==|")
  print("|==                                      ==|")
  print("|==        0-Sair                        ==|")
  print("|==                                      ==|")
  print("|==========================================|")
  print("|==========================================|")
  option = input("|= Escolha uma opção: ")
  if option == "1":
    option_clt = ''
    while option_clt != "0":
        limpar_tela()
        print("|==========================================|")
        print("|=========== Módulo de Clientes ===========|")
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==        1-Cadastrar clientes          ==|")
        print("|==                                      ==|")
        print("|==        2-Buscar clientes             ==|")
        print("|==                                      ==|")
        print("|==        3-Editar clientes             ==|")
        print("|==                                      ==|")
        print("|==        4-Remover clientes            ==|")
        print("|==                                      ==|")
        print("|==        0-Sair                        ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==========================================|")
        option_clt = input("|= Escolha uma opção: ")
        if option_clt == "1":
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
        elif option_clt == "2":
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
        elif option_clt == "3":
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
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Cliente editado com sucesso!!    ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                     elif option3_clt == "2":
                        phone_clt = input("|== Digite o novo telefone do cliente: ")
                        clientes[cpf_clt][1] = phone_clt
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Cliente editado com sucesso!!    ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                     elif option3_clt == "3":
                        cpf_antigo = cpf_clt
                        cpf_clt = input("|= Digite o novo CPF do cliente: ")
                        if cpf_clt in clientes:
                           print("|==========================================|")
                           print("|==                                      ==|")
                           print("|==       CPF inválido ou em uso!        ==|")
                           print("|==                                      ==|")
                           print("|==========================================|")
                        elif cpf_clt == "":
                           print()
                        else:
                           clientes[cpf_clt] = [clientes[cpf_antigo][0], clientes[cpf_antigo][1], clientes[cpf_antigo][2]]
                           del clientes[cpf_antigo]
                           print("|==========================================|")
                           print("|==                                      ==|")
                           print("|==     Cliente editado com sucesso!!    ==|")
                           print("|==                                      ==|")
                           print("|==========================================|")
                     elif option3_clt == "4":
                        city_clt = input("|== Digite a nova cidade do cliente: ")
                        clientes[cpf_clt][2] = city_clt
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
        elif option_clt == "4":
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
        elif option_clt == "0":
           option_clt = "0"
        else:
           print()
  elif option == "2":
    option_cnt = ''
    while option_cnt != "0":
        limpar_tela()
        print("|==========================================|")
        print("|============ Módulo de Contas ============|")
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==     1-Adicionar conta                ==|")
        print("|==                                      ==|")
        print("|==     2-Buscar contas do cliente       ==|")
        print("|==                                      ==|")
        print("|==     3-Editar valores de uma conta    ==|")
        print("|==                                      ==|")
        print("|==     4-Remover conta                  ==|")
        print("|==                                      ==|")
        print("|==     0-Sair                           ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==========================================|")
        option_cnt = input("|= Escolha uma opção: ")
        if option_cnt == "1":
           cpf_cnt = input("|= Digite o CPF do cliente: ")
           if cpf_cnt in clientes:
              desc_cnt = input("|= Digite a descrição da conta: ")
              valor_cnt = input("|= Digite o valor da conta: ")
              venc_cnt = input("|= Digite a data de vencimento da conta: ")
              contas[cpf_cnt] = [desc_cnt, valor_cnt, venc_cnt]
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
        elif option_cnt == "2":
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
                input("|== Voltar para o Módulo de contas <Enter>: ")
        elif option_cnt == "3":
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
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Conta editada com sucesso!!      ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                     elif option3_cnt == "2":
                        debito_cnt = input("|== Digite o novo débito da conta: ")
                        contas[cpf_cnt][1] = debito_cnt
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
                        elif cpf_cnt == "":
                           print()
                        else:
                           contas[cpf_cnt] = [contas[cpf_antigo][0], contas[cpf_antigo][1], contas[cpf_antigo][2]]
                           del contas[cpf_antigo]
                           print("|==========================================|")
                           print("|==                                      ==|")
                           print("|==     Conta editada com sucesso!!      ==|")
                           print("|==                                      ==|")
                           print("|==========================================|")
                     elif option3_cnt == "4":
                        vencimento_cnt = input("|== Digite o novo vencimento da conta: ")
                        contas[cpf_cnt][2] = vencimento_cnt
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
        elif option_cnt == "4":
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
        elif option_cnt == "0" or option_cnt == "":
           print()
        else:
            print("|==========================================|")
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==       Módulo em desenvolvimento      ==|")
            print("|==                                      ==|")
            print("|==========================================|")
            print("|==========================================|")
            input("|= Voltar para o Módulo de contas <Enter>: ")

  elif option == "3":
    option_pmt = ''
    while option_pmt != "0":
        limpar_tela()
        print("|==========================================|")
        print("|========== Módulo de Pagamentos ==========|")
        print("|==========================================|")
        print("|==                                      ==|")
        print("|==     1-Registrar pagamentos           ==|")
        print("|==                                      ==|")
        print("|==     2-Ver histórico de pagamento     ==|")
        print("|==                                      ==|")
        print("|==     3-Remover registros              ==|")
        print("|==                                      ==|")
        print("|==     3-Editar registros               ==|")
        print("|==                                      ==|")
        print("|==     0-Sair                           ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==========================================|")
        option_pmt = input("|= Escolha uma opção: ")
        if option_pmt == "0":
           print()
        else:
            print("|==========================================|")
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==       Módulo em desenvolvimento      ==|")
            print("|==                                      ==|")
            print("|==========================================|")
            print("|==========================================|")
            input("|= Voltar para o Módulo de pagamentos <Enter>: ")
  elif option == "4":
    limpar_tela()
    print("|==========================================|")
    print("|========== Módulo de Informações =========|")
    print("|==========================================|")
    print("|==                                      ==|")
    print("|==     Projeto de Gestão de Clientes    ==|")
    print("|==                                      ==|")
    print("|==     Autor do projeto:                ==|")
    print("|==     ↳ Francisco Talismar             ==|")
    print("|==                                      ==|")
    print("|==     Licença Pública Geral GNU        ==|")
    print("|==     ↳ www.gnu.org/licenses/gpl.html  ==|")
    print("|==                                      ==|")
    print("|==========================================|")
    print("|==========================================|")
    option_inv = input("|= Voltar para o Módulo principal <Enter>: ")
  elif not option:
     print()
  elif option == "0":
     fechar = input("|= Tem certeza que deseja sair? (S/N): ")
     if fechar.upper() == "S":
        limpar_tela()
        print("Fim do programa!!")    
     else:
        option = ''
  else:
    limpar_tela()
    print("|==========================================|")
    print("|==========================================|")
    print("|==                                      ==|")
    print("|==           Opção inválida!!           ==|")
    print("|==                                      ==|")
    print("|==========================================|")
    print("|==========================================|")
    option_inv = input("|= Voltar para o Módulo principal <Enter>: ")