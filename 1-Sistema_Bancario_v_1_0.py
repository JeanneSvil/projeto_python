menu = """ 
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
  opcao = input(menu)
  if opcao == "1":
    print("Depósito")
    valor = float(input("Qual o valor do depósito desejado? "))
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

    if valor > 0:
      print(f"""Depósito de R${valor:.2f} realizado com sucesso!
      Saldo total: R${saldo:.2f}
      """)
      #break
        
    else:
      print("Valor inválido! Tente novamente.")

  elif opcao == "2":
    print("Sacar")
    print("Saque")
    while numero_saques < LIMITES_SAQUES:
      valor = float(input("Qual o valor que deseja sacar? "))
      
      if valor <= limite:
        if valor > 0 and valor<= saldo:
          numero_saques += 1
          extrato += f"Saque: R$ {valor:.2f}\n"
          print(f"""Saque número {numero_saques} de R${valor:.2f} realizado com sucesso!
          Saldo total: R${saldo - valor:.2f}
  """)
          saldo -= valor
          break

        elif valor > saldo:
          print("Não será possível sacar o dinheiro por falta de saldo.")
        elif valor <= 0:
          print ("O valor informado é inválido.")

      else:
        print("O valor do saque excede o limite.")

    if numero_saques == LIMITES_SAQUES:
      print("Número máximo de saque atingido!!!")

  elif opcao == "3":
    print("\n========= Extrato =========")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"Saldo atual: R${saldo:.2f}")
    print("=============================")

  elif opcao == "0":
    break

  else:
    print(f"Operação inválida, por favor selecione novamente a operação desejada")

