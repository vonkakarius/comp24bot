import telepot
from dados import TOKEN, nick_bot


bot = telepot.Bot(TOKEN)


class Message:
    '''Classe que representa uma mensagem recebida'''
    def __init__(self, text: str, userId: int, userName: str, chatId: int, date: int) -> None:
        self.text = text
        self.userId = userId
        self.userName = userName
        self.chatId = chatId
        self.date = date


def enviar(text: str, chatId: int) -> None:
    '''Envia mensagem de texto para o chat especificado'''
    bot.sendMessage(chatId, text, parse_mode='Markdown')


def gerarComandos(*commands: str) -> list[str]:
    '''Recebe nomes de comandos e devolve uma lista de palavras-chaves aceitáveis pelo bot'''
    commandsList: list[str] = []

    for commandName in commands:
        commandsList.append(f'/{commandName}')
        commandsList.append(f'/{commandName}@{nick_bot}')

    return commandsList


def extrairComando(text: str) -> tuple[str, list[str]]:
    '''Extrai comando e parâmetros de uma mensagem'''
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