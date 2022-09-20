from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler

from compbot.handlers.decorators import create_handler
from compbot.handlers.exception import UserError
from compbot.services import roll_services


@create_handler(handler_type=CommandHandler, command='roll')
async def roll(update: Update, context: CallbackContext):
    if not context.args:
        raise UserError(
            description='User did not provide roll string as argument',
            reply_message='Qual jogada tenho que fazer?\n\n'
                          'Exemplos: <code>1d6</code> ou <code>1d4+5</code>',
            parse_mode=ParseMode.HTML
        )
    roll_str = ' '.join(context.args)
    roll_parsed = roll_services.parse_roll_str(roll_str=roll_str)
    roll_result = roll_services.roll(*roll_parsed)
    message = f'<b>Resultado:</b> {roll_result}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

