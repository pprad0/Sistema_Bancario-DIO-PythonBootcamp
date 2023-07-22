import bancoDeDados as db


def validar_cpf():
    cpf = input("CPF: ")

    cpf_formatado = cpf.replace(".", "").replace("-", "")

    if not len(cpf_formatado) == 11:
        print("CPF inválido. O CPF deve conter 11 números, exemplo: 123.123.123-20")
        return False

    for user in db.usuarios:
        if cpf_formatado in user[cpf]:
            return print("Erro: Usuário já cadastrado em nosso banco de dados.")

    return cpf_formatado


def dados_do_usuario(cpf):
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Data de nascimento: (dd/mm/aaaa) ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla) : ")

    endereco = f"{logradouro}, {numero}, bairro {bairro}, {cidade}/{estado}"

    return {nome, data_nascimento, endereco, cpf}
