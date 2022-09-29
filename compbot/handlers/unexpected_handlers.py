from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, filters

from compbot.utils.decorators import create_handler


@create_handler(handler_type=MessageHandler, filters=filters.COMMAND)
async def reply_unknown_command(update: Update, context: CallbackContext):
    """
    Handler called whenever the user sends an unknown command.

    Replies the caller with a friendly message and should be the last command handler added.
    """
    # Get inputted command and remove any words the user might have sent after it
    command = update.effective_message.text.split(" ")[0]
    # Send message
    message = f'Não conheço o comando {command} ainda :('
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
