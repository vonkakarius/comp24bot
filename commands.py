from utils import Message, extrairComando, gerarComandos, enviar


def darOi(msg: Message) -> None:
    '''Dá oi para o usuário'''
    enviar(f'Oi, {msg.userName}!', msg.chatId)


def processar(msg: Message) -> None:
    '''Interpreta uma mensagem recebida'''
    command, parameters = extrairComando(msg.text)

    # Encaminha de acordo com o comando
    try:
        if command in gerarComandos('oi'):
            darOi(msg, *parameters)
    except Exception as erro:
        print(erro)