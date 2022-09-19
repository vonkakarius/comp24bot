from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from compbot.handlers.decorators import create_handler
from compbot.services import roll_services


# TODO: implement error handling for lack or inconsistency of user arguments
@create_handler(handler_type=CommandHandler, command='roll')
async def roll(update: Update, context: CallbackContext):
    if not context.args:
        return
    roll_str = ' '.join(context.args)
    roll_parsed = roll_services.parse_roll_str(roll_str=roll_str)
    roll_result = roll_services.roll(*roll_parsed)
    message = f'**Resultado**: {roll_result}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='MarkdownV2')

