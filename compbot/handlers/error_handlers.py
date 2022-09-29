import json
import html
from math import ceil
from traceback import format_exception

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from compbot.utils.exceptions import UserError


DEV_CHAT_ID = -1001593083775


async def handle_user_error(update: Update, context: CallbackContext, error: UserError):
    """
    Handles exceptions that are instances of UserError (or derived classes).

    If a reply message was defined by the developer that created the exception, \
    send a reply in the chat that sent the error-causing message.
    """
    if error.reply_message is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=error.reply_message,
            parse_mode=error.parse_mode
        )


async def build_general_error_message(update, context: CallbackContext) -> str:
    """
    Builds an HTML message for unexpected errors to be sent to the dev team.

    The message contains data on
    - the update where the exception occurred
    - the chat from where the message was sent
    - the user who sent the message
    - the exception traceback
    """
    # format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    traceback_string = "".join(format_exception(None, context.error, context.error.__traceback__))
    # Build the message with some markup and additional information about what happened.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f'An exception was raised while handling an update\n\n'
        f'<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}</pre>\n\n'
        f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
        f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
        f'<pre>{html.escape(traceback_string)}</pre>'
    )
    return message


async def send_general_error_message_to_devs(context: CallbackContext, message: str):
    """
    Sends error message to dev team.

    Sends an HTML message to dev team informing them of an unexpected error. Additionally, \
    if the message exceeds the 4 kB limit imposed by telegram, then it is paginated into \
    smaller chunks before being sent.
    """
    # Get number of bytes of the string (length in UTF-8 encoding)
    size = len(message.encode('utf-8'))
    # Paginate message in chunks (pages) smaller than 4 kB (4096 B)
    num_pages = 1
    while size / num_pages >= 4096:
        num_pages += 1
    page_size = ceil(len(message) / num_pages)
    pages = [message[page_size*i:page_size*(i+1)] for i in range(num_pages)]
    # Send each page to the dev team (telegram sends up to 4 kB in a single message)
    for page in pages:
        await context.bot.send_message(chat_id=DEV_CHAT_ID, text=page, parse_mode=ParseMode.HTML)


async def handle_general_error(update, context: CallbackContext):
    """
    Handles general (unexpected) server side errors.

    It sends a message to the dev team with a full description of update where the error occurred \
    and the complete traceback of the caught error. It also sends a short reply to the user informing \
    them of an unexpected error.
    """
    message_devs = await build_general_error_message(update=update, context=context)
    # Send a full log of the error to the dev team
    await send_general_error_message_to_devs(context=context, message=message_devs)
    # Inform the user of an internal error
    if isinstance(update, Update):
        message_user = 'Desculpe, ocorreu um erro inesperado :('
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_user)


async def error_handler(update, context: CallbackContext):
    """
    Handles exceptions raised at runtime.

    If the exception is of type UserError (that is, it is an instance of the UserError \
    class or of any class in its hierarchy), the user may receive a predefined reply \
    message explaining the correct usage, and no logs should be sent to the dev team. \
    If an error was generated from any other cause, then the dev team should be notified \
    of the anomaly via the chat specified in the constant DEV_CHAT_ID, and the user should \
    receive a message informing them of the internal error.
    """
    if isinstance(update, Update) and isinstance(context.error, UserError):
        await handle_user_error(update=update, context=context, error=context.error)
    else:
        await handle_general_error(update=update, context=context)
