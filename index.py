import controllers.conta as conta

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
        conta.depositar()

    elif escolha == "2":
        conta.sacar()

    elif escolha == "3":
        conta.ver_extrato()

    elif escolha == "4":
        break

print(
    """
      Volte sempre!
    """
)
