import bancoDeDados as db


def validar_cpf():
    cpf = input("CPF: ")

    cpf_formatado = cpf.replace(".", "").replace("-", "")

    if not len(cpf_formatado) == 11:
        print(
            "<Erro>: CPF inválido. O CPF deve conter 11 números, exemplo: 123.123.123-20"
        )
        return False

    for user in db.usuarios:
        if cpf_formatado in user["dados"]["cpf"]:
            return print("<Erro>: Usuário já cadastrado em nosso banco de dados.")

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

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "cpf": cpf,
    }
    db.usuario_id += 1

    return usuario


def dados_conta_bancária():
    usuario_id = input("Informe o seu ID de usuário: ")

    if usuario_id is None:
        return print("<Erro>: ID de usuário não pode ser vazio.")

    usuario_id = int(usuario_id)

    usuario_existe = False
    for i in db.usuarios:
        if usuario_id == i["usuario_id"]:
            usuario_existe = True
            break

    if not usuario_existe:
        return print("<Erro>: Informe outro ID de usuário, o informado não existe.")

    return usuario_id
