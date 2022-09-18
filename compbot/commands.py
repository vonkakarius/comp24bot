from utils import Message, extrair_comando, gerar_comandos, enviar


def dar_oi(msg: Message) -> None:
    '''Dá oi para o usuário'''
    enviar(f'Oi, {msg.username}!', msg.chat_id)


def processar(msg: Message) -> None:
    '''Interpreta uma mensagem recebida'''
    command, parameters = extrair_comando(msg.text)

    # Encaminha de acordo com o comando
    try:
        if command in gerar_comandos('oi'):
            dar_oi(msg, *parameters)
    except Exception as erro:
        print(erro)
