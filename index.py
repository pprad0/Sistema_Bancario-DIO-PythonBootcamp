import controllers.conta as conta
import controllers.usuario as usuario

menu = """
    ----- MENU -----
    
    Você gostaria de:
    
    [1] Cadastrar usuário 
    [2] Cadastrar conta
    [3] Depositar
    [4] Sacar
    [5] Ver extrato
    [6] Sair
        
        """


while True:
    escolha = input(menu)

    if escolha == "1":  # cadastro usuário
        usuario.cadastrar_usuario()

    elif escolha == "2":  # cadastro conta
        usuario.cadastrar_conta_bancaria()

    elif escolha == "3":  # deposito
        conta.depositar()

    elif escolha == "4":  # saque
        conta.sacar()

    elif escolha == "5":  # extrato
        conta.ver_extrato()

    elif escolha == "6":  # sair
        break

print(
    """
      Volte sempre!
    """
)
