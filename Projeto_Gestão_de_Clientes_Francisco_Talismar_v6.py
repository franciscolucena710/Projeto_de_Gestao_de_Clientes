import os
import ast
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def save():
    arq = open('clientes.txt', 'w', encoding='utf-8')
    for cliente in clientes:
        arq.write(cliente + '\n')
        for info in clientes[cliente]:
            arq.write(info + '\n')
    arq.close()
    arq2 = open('contas.txt', 'w', encoding='utf-8')
    for conta in contas:
        arq2.write(conta + '\n')
        for info in contas[conta]:
            arq2.write(info + '\n')
    arq2.close()
    arq3 = open('pagamentos.txt', 'w', encoding='utf-8')
    arq3.write(str(pagamentos))
    arq3.close()

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
arq = open('pagamentos.txt', 'r', encoding='utf-8')
conteudo_do_arquivo = arq.read()
arq.close()
pagamentos = ast.literal_eval(conteudo_do_arquivo)
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
               save()
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
                        save()
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Cliente editado com sucesso!!    ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                     elif option3_clt == "2":
                        phone_clt = input("|== Digite o novo telefone do cliente: ")
                        clientes[cpf_clt][1] = phone_clt
                        save()
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
                           save()
                           print("|==========================================|")
                           print("|==                                      ==|")
                           print("|==     Cliente editado com sucesso!!    ==|")
                           print("|==                                      ==|")
                           print("|==========================================|")
                     elif option3_clt == "4":
                        city_clt = input("|== Digite a nova cidade do cliente: ")
                        clientes[cpf_clt][2] = city_clt
                        save()
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
                  save()
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
              save()
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
                        save()
                        print("|==========================================|")
                        print("|==                                      ==|")
                        print("|==     Conta editada com sucesso!!      ==|")
                        print("|==                                      ==|")
                        print("|==========================================|")
                     elif option3_cnt == "2":
                        debito_cnt = input("|== Digite o novo débito da conta: ")
                        contas[cpf_cnt][1] = debito_cnt
                        save()
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
                           save()
                           print("|==========================================|")
                           print("|==                                      ==|")
                           print("|==     Conta editada com sucesso!!      ==|")
                           print("|==                                      ==|")
                           print("|==========================================|")
                     elif option3_cnt == "4":
                        vencimento_cnt = input("|== Digite o novo vencimento da conta: ")
                        contas[cpf_cnt][2] = vencimento_cnt
                        save()
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
                  save()
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
            print("|==           Opção inválida!!           ==|")
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
        print("|==     1-Pagar contas                   ==|")
        print("|==                                      ==|")
        print("|==     2-Ver registros de pagamentos    ==|")
        print("|==                                      ==|")
        print("|==     3-Remover registros              ==|")
        print("|==                                      ==|")
        print("|==     4-Editar registros               ==|")
        print("|==                                      ==|")
        print("|==     0-Sair                           ==|")
        print("|==                                      ==|")
        print("|==========================================|")
        print("|==========================================|")
        option_pmt = input("|= Escolha uma opção: ")
        if option_pmt == "1":
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
               save()
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
        elif option_pmt == "2":
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
        elif option_pmt == "3":
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
                 save()
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
        elif option_pmt == "4":
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
                             save()
                             print("|==========================================|")
                             print("|==                                      ==|")
                             print("|==     Pagamento editado com sucesso!!  ==|")
                             print("|==                                      ==|")
                             print("|==========================================|")
                          elif option4_pmt == "2":
                             debito_pmt = input("|== Digite o novo débito do pagamento: ")
                             pagamentos[cpf_pmt][registro_pmt_int][1] = debito_pmt
                             save()
                             print("|==========================================|")
                             print("|==                                      ==|")
                             print("|==     Pagamento editado com sucesso!!  ==|")
                             print("|==                                      ==|")
                             print("|==========================================|")
                          elif option4_pmt == "3":
                              vencimento_pmt = input("|== Digite o novo vencimento do pagamento: ")
                              pagamentos[cpf_pmt][registro_pmt_int][2] = vencimento_pmt
                              save()
                              print("|==========================================|")
                              print("|==                                      ==|")
                              print("|==     Pagamento editado com sucesso!!  ==|")
                              print("|==                                      ==|")
                              print("|==========================================|")
                          elif option4_pmt == "4":
                              data_pmt = input("|== Digite a nova data do pagamento: ")
                              pagamentos[cpf_pmt][registro_pmt_int][3] = data_pmt
                              save()
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
                                                
        elif option_pmt == "0":
           print()
        else:
            print("|==========================================|")
            print("|==========================================|")
            print("|==                                      ==|")
            print("|==           Opção inválida!!           ==|")
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