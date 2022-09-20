import json
import html
from traceback import format_exception
from sys import stderr

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext


DEVELOPER_CHAT_ID = 904163238


class UserError(Exception):
    """Exception to be thrown by a handler if there is a user side error."""

    def __init__(
            self, description: str = '',
            reply_message: str | None = None,
            parse_mode: ParseMode = ParseMode.MARKDOWN
    ) -> None:
        self.description = description
        self.reply_message = reply_message
        self.parse_mode = parse_mode

    def __str__(self):
        print(self.description, file=stderr)


async def error_handler(update, context: CallbackContext):
    if isinstance(update, Update) and isinstance(context.error, UserError):
        # If it was a handler user error, return a message to the user
        if context.error.reply_message:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=context.error.reply_message,
                parse_mode=context.error.parse_mode
            )
    else:
        # format_exception returns the usual python message about an exception, but as a
        # list of strings rather than a single string, so we have to join them together.
        tb_string = "".join(format_exception(None, context.error, context.error.__traceback__))
        # Build the message with some markup and additional information about what happened.
        update_str = update.to_dict() if isinstance(update, Update) else str(update)
        message = (
            f'An exception was raised while handling an update\n'
            f'<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}'
            '</pre>\n\n'
            f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
            f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
            f'<pre>{html.escape(tb_string)}</pre>'
        )
        # TODO: send message to developer team
        await context.bot.send_message(chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML)

