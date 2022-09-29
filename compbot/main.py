import logging
from argparse import ArgumentParser
from os import environ

from telegram.ext import ApplicationBuilder

from compbot.api import add_api


if __name__ == '__main__':
    # Add argument parser
    parser = ArgumentParser(description='Get configuration and sensitive data from server')
    parser.add_argument('token', help='token used to control bot')
    parser.add_argument(
        '-p', '--production',
        help='set if process is run in production server',
        action='store_true'
    )
    args = parser.parse_args()
    # Setup logger
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    # Build application
    application = ApplicationBuilder().token(args.token).build()
    # Add command API
    add_api(application=application, in_prod=args.production)
    # Start server application
    application.run_polling()


