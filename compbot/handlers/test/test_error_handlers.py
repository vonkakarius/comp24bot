from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from compbot.utils.decorators import create_handler
from compbot.utils.exceptions import UserError


@create_handler(handler_type=CommandHandler, command='test_user_error')
async def test_user_error(update: Update, context: CallbackContext):
    """Raises a user error"""
    raise UserError(
        description='generic user error',
        reply_message='Você cometeu um erro!'
    )


@create_handler(handler_type=CommandHandler, command='test_unexpected_error')
async def test_unexpected_error(update: Update, context: CallbackContext):
    """Raises a generic exception"""
    raise Exception('Generic exception')
