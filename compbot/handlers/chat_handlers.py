from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.constants import ParseMode

from compbot.utils.decorators import create_handler


@create_handler(handler_type=CommandHandler, command='getchatid')
async def get_chat_id(update: Update, context: CallbackContext):
    """Sends back the id of the chat"""
    message = (
        f'ID do chat **{update.message.chat.title}**:\n\n'
        f'{update.effective_chat.id}'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        parse_mode=ParseMode.MARKDOWN
    )