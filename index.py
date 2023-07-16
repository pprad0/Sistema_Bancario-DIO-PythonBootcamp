extrato = ""

LIMITE_SAQUES = 3
saques_realizados = 0
saldo = 0

menu = """
    ----- MENU -----
    
    Você gostaria de:
    
    [1] Depositar
    [2] Sacar
    [3] Ver extrato
    [4] Sair
        
        """


while True:
    escolha = input(menu)

    if escolha == "1":
        valor = int(input(" Insira o valor do depósito:  "))

        if float(valor) <= 0:
            print(
                """
                  
                  Falha no processo, o valor precisa ser maior que zero.
                  
                  """
            )
        else:
            extrato += f"Depósito de R${valor: .2f} \n"
            saldo += valor
            print(
                """
                  Deposito feito com sucesso! Retornando ao menu.
                  """
            )

    if escolha == "2":
        if saques_realizados < LIMITE_SAQUES:
            saque = float(
                input(
                    """
                    Qual o valor do saque? O seu limite é: R$500,00
                """
                )
            )

            if saque <= 500 and saldo - saque >= 0:
                saldo -= saque
                extrato += f"Saque de R${saque: .2f} \n"
                saques_realizados += 1
                print(
                    """
                      Saque realizado com sucesso!
                    """
                )

            else:
                print(
                    """
                    Saldo insuficiente ou valor limite de saque alcançado.
                    """
                )

        else:
            print(
                """ 
                  Limite diário de saques alcançado, volte amanhã.
                  """
            )

    if escolha == "3":
        print(extrato)
        print(f"Seu saldo é R${saldo: .2f}")

    if escolha == "4":
        break

print(
    """
      Volte sempre!
      """
)
