import os
import mod1
import mod2
import mod3
from mod1 import limpar_tela
from memoryt import load
import mod1
clientes, contas, pagamentos = load()
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
            mod1.cadastrar(clientes)
        elif option_clt == "2":
            mod1.buscar(clientes)
        elif option_clt == "3":
            mod1.editar(clientes)
        elif option_clt == "4":
            mod1.remover(clientes)
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
           mod2.cadastrar(contas,clientes)
        elif option_cnt == "2":
           mod2.buscar(contas,clientes)
        elif option_cnt == "3":
           mod2.editar(contas,clientes)  
        elif option_cnt == "4":
           mod2.remover(contas,clientes)                      
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
           mod3.cadastrar(pagamentos,contas,clientes)
        elif option_pmt == "2":
           mod3.buscar(pagamentos,clientes)
        elif option_pmt == "3":
           mod3.remover(pagamentos,clientes)
        elif option_pmt == "4":
           mod3.editar(pagamentos,clientes)                               
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