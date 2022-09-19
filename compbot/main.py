import logging
from sys import argv
from telegram.ext import ApplicationBuilder

from compbot.api import add_api


def get_token() -> str:
    if len(argv) < 2:
        raise ValueError('Provide bot token as a command line argument')
    return argv[1]


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    token = get_token()
    # Build application
    application = ApplicationBuilder().token(token).build()
    # Add command API
    add_api(application=application)
    # Start server application
    application.run_polling()


