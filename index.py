import controllers.conta as conta
import controllers.usuario as usuario

menu = """
    ----- MENU -----
    
    Você gostaria de:
    
    [1] Depositar
    [2] Sacar
    [3] Ver extrato
    [4] Cadastrar usuário
    [5] Sair
        
        """


while True:
    escolha = input(menu)

    if escolha == "1":
        valor = int(input(" Insira o valor do depósito:  "))
        conta.depositar(valor)

    elif escolha == "2":
        conta.sacar()

    elif escolha == "3":
        conta.ver_extrato()

    elif escolha == "4":
        usuario.cadastrar_usuario()

    elif escolha == "5":
        break

print(
    """
      Volte sempre!
    """
)
