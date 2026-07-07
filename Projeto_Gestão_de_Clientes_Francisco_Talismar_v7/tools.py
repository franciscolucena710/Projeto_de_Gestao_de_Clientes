from datetime import datetime
def valida_cpf(cpf):
  tam = len(cpf)
  soma = 0
  d1 = 0
  d2 = 0
  if tam != 11:
    return False
  for i in range(11):
    if (cpf[i]<'0')or(cpf[i]>'9'):
      return False
  for i in range(9):
    soma += (int(cpf[i])*(10 - i))
  d1 = 11 - (soma % 11)
  if (d1 == 10 or d1 == 11):
    d1 = 0
  if d1 != int(cpf[9]):
    return False
  soma = 0
  for i in range(10):
    soma += (int(cpf[i])*(11-i))
  d2 = 11 - (soma%11)
  if (d2 == 10 or d2 == 11):
    d2 = 0
  if d2 != int(cpf[10]):
    return False
  return True

def valida_phone(phone,clientes):
  tam = len(phone)
  if tam < 10 or tam > 11:
    return False
  for i in range(tam):
    if (phone[i]<'0')or(phone[i]>'9'):
      return False
  for cliente in clientes:
    if clientes[cliente][1] == phone:
      return False
  return True

def validar_data(data: str):
    apenas_numeros = "".join(char for char in data if char.isdigit())

    if len(apenas_numeros) != 8:
        return None  

    dia = apenas_numeros[0:2]
    mes = apenas_numeros[2:4]
    ano = apenas_numeros[4:8]
    
    data_formatada = f"{dia}-{mes}-{ano}"
    
    try:
        datetime.strptime(data_formatada, "%d-%m-%Y")
        return data_formatada
    except ValueError:
        return None