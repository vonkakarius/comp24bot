from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from compbot.handlers.decorators import create_handler
from compbot.services import greet_services


@create_handler(handler_type=CommandHandler, command='oi')
async def simple_greet(update: Update, context: CallbackContext):
    caller_first_name = update.message.chat.first_name
    message = greet_services.get_simple_greet_str(first_name=caller_first_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


@create_handler(handler_type=CommandHandler, command='ola')
async def complex_greet(update: Update, context: CallbackContext):
    caller_full_name = update.message.chat.full_name
    message = greet_services.get_complex_greet_str(full_name=caller_full_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# TODO: implement error handling in case no arguments are passed
@create_handler(handler_type=CommandHandler, command='cumprimente')
async def greet_someone(update: Update, context: CallbackContext):
    if not context.args:
        return
    target_name = context.args[0]
    message = greet_services.get_simple_greet_str(first_name=target_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
