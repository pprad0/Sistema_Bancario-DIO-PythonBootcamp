import validacoes.cadastroUsuario as validacao
import bancoDeDados as db


def cadastrar_usuario():
    cpf = validacao.validar_cpf()
    if not cpf:
        return

    dados = validacao.dados_do_usuario(cpf)

    # inserir no banco de dados
    novo_usuario = {"usuario_id": db.usuario_id, "dados": dados}  # formatação
    db.usuarios.append(novo_usuario)  # inserção

    print(
        f"""
    ---------------------------------------------     
    Usuário cadastrado com sucesso!
     
    Anote o ID do usuário: {db.usuario_id}
    ---------------------------------------------
        """
    )
    return


def cadastrar_conta_bancaria():
    usuario_id = validacao.dados_conta_bancária()

    if usuario_id:
        agencia = db.AGENCIA
        db.conta_id += 1
        conta_id = db.conta_id

        nova_conta = [agencia, conta_id, usuario_id]
        db.contas.append(nova_conta)

    return
