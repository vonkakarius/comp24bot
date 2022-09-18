import telepot
from compbot.botdata import TOKEN, nick_bot


bot = telepot.Bot(TOKEN)


class Message:
    """Classe que representa uma mensagem recebida"""
    def __init__(self, text: str, user_id: int, username: str, chat_id: int, date: int) -> None:
        self.text = text
        self.user_id = user_id
        self.username = username
        self.chat_id = chat_id
        self.date = date


def enviar(text: str, chat_id: int) -> None:
    """Envia mensagem de texto para o chat especificado"""
    bot.sendMessage(chat_id, text, parse_mode='Markdown')


def gerar_comandos(*commands: str) -> list[str]:
    """Recebe nomes de comandos e devolve uma lista de palavras-chaves aceitáveis pelo bot"""
    commands_list: list[str] = []

    for commandName in commands:
        commands_list.append(f'/{commandName}')
        commands_list.append(f'/{commandName}@{nick_bot}')

    return commands_list


def extrair_comando(text: str) -> tuple[str, list[str]]:
    """Extrai comando e parâmetros de uma mensagem"""
    try:
        params = text.lower().split()
        command = params[0]
        params = params[1:]
        for i, item in enumerate(params):
            try:
                params[i] = int(item)
            except:
                continue
        return command, params
    except:
        return text.lower(), []