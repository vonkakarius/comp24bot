from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler

from compbot.utils.decorators import create_handler
from compbot.exceptions.roll_exceptions import NoRollStr
from compbot.services import roll_services
from compbot.schemas.roll_schemas import RollStr


@create_handler(handler_type=CommandHandler, command='roll')
async def roll(update: Update, context: CallbackContext):
    if not context.args:
        raise NoRollStr()
    roll_str = RollStr(' '.join(context.args))
    roll_result = roll_services.roll(roll_str)
    message = f'<b>Resultado:</b>\n {roll_result}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
