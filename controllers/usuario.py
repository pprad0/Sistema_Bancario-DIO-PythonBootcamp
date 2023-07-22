import validacoes.cadastroUsuario as validacao
import bancoDeDados as db


def cadastrar_usuario():
    cpf = validacao.validar_cpf()
    if not cpf:
        return

    dados = validacao.dados_do_usuario(cpf)
    db.usuarios.append(dados)
    print(db.usuarios)


def cadastrar_conta_bancaria():
    print("")
