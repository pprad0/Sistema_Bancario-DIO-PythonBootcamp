extrato = ""

LIMITE_SAQUES = 3
saques_realizados = 0
saldo = 0


# assertar  parâmetros


def depositar(valor):
    if float(valor) <= 0:
        return print(
            """
              
              Falha no processo, o valor precisa ser maior que zero.
              
              """
        )
    else:
        global extrato, saldo

        extrato += f"Depósito de R${valor: .2f} \n"
        saldo += valor

        return print(
            """
              Deposito feito com sucesso! Retornando ao menu.
            """
        )


def sacar():
    global LIMITE_SAQUES, saldo, saques_realizados, extrato

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


def ver_extrato():
    print(
        """
---------------------------------------
        """
    )

    print(extrato)
    print(f"Seu saldo é R${saldo: .2f}")

    print(
        """
---------------------------------------
        """
    )
