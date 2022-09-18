import telepot
import urllib3
import commands
from flask import Flask, request

from compbot.botdata import nick, TOKEN, segredo
from compbot.utils import Message

# -------------------------------------------------------------------
#  CONEXÃO
# -------------------------------------------------------------------


proxy_url = 'http://proxy.server:3128'
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
app = Flask(__name__)

bot = telepot.Bot(TOKEN)
bot.setWebhook(f'https://{nick}.pythonanywhere.com/{segredo}', max_connections=1)


# -------------------------------------------------------------------
# NOVA MENSAGEM
# -------------------------------------------------------------------


@app.route(f'/{segredo}', methods=['POST'])
def telegram_webhook():
    # Recebe a atualização
    update = request.get_json()
    # Faz o log dela
    print('NOVA ATUALIZAÇÃO\n\n')
    print(update)

    # Trabalha na mensagem
    if 'message' in update:
        # Captura legenda de mídia
        if 'caption' in update['message']:
            update['message']['text'] = update['message']['caption']

        # Processa mensagem em texto
        if 'text' in update['message']:
            try:
                text: str = update['message']['text']
                user_id: int = update['message']['from']['id']
                username: str = update['message']['from']['first_name']
                chat_id: int = update['message']['chat']['id']
                date: int = update['message']['date']
                
                # Processa a mensagem
                commands.processar(Message(text, user_id, username, chat_id, date))
            except Exception as erro:
                print(erro)

    return 'OK'
