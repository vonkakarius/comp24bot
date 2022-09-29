from telegram.ext import Application

from compbot.handlers import (
    greet_handlers,
    roll_handlers,
    unexpected_handlers,
    chat_handlers,
    error_handlers
)


def add_api(application: Application):
    """
    Telegram bot project. This is an amazing description of what it is.

    Supported commands:
        /oi: greets caller with 'Oi, {caller_name}!'
        /ola: greets caller with 'Olá, {caller_full_name}, tenha um ótimo dia!'
        /cumprimente {name}: greets someone with 'Oi, {name}|'
        /roll {AdB [+/- C]}: executes dice rolls and adds a modifier
        /getchatid: return id of the current chat
    """
    # Add chat handlers
    application.add_handler(chat_handlers.get_chat_id)
    # Add greet handlers
    application.add_handler(greet_handlers.simple_greet)
    application.add_handler(greet_handlers.complex_greet)
    application.add_handler(greet_handlers.greet_someone)
    # Add roll handlers
    application.add_handler(roll_handlers.roll)
    # Add unknown command handler
    application.add_handler(unexpected_handlers.reply_unknown_command)
    # Add error handler
    application.add_error_handler(error_handlers.error_handler)
