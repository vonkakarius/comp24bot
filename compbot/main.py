import logging
from sys import argv
from telegram.ext import ApplicationBuilder

from compbot.handlers import greet_handlers
from compbot.handlers import roll_handlers

"""
Telegram bot project. This is an amazing description of what it is.

Supported commands:
    /oi: greets caller with 'Oi, {caller_name}!'
    /ola: greets caller with 'Olá, {caller_full_name}, tenha um ótimo dia!'
    /cuprimente {name}: greets someone with 'Oi, {name}|'
    /roll {AdB [+/- C]}: executes dice rolls and adds a modifier 
"""


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    # Get bot token
    if len(argv) < 2:
        raise ValueError('Provide bot token as a command line argument')
    token = argv[1]
    print(f'Connecting to {token}')
    # Build application
    application = ApplicationBuilder().token(token).build()
    # Add greet handlers
    application.add_handler(greet_handlers.simple_greet)
    application.add_handler(greet_handlers.complex_greet)
    application.add_handler(greet_handlers.greet_someone)
    # Add roll handlers
    application.add_handler(roll_handlers.roll)
    # Start server application
    application.run_polling()


