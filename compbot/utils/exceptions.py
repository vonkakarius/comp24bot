from telegram.constants import ParseMode


class UserError(Exception):
    """
    Exception to be thrown by a handler if there is a user side error.

    A reply message should be given during initialization, alongside a parsing method, with \
    a nice explanation of the error to the user and, optionally, examples of correct usage. \
    That way, the global error handler will be able to send the reply message to the caller \
    whenever an error occurs in a consistent manner. If no reply message should be sent to \
    the user, then reply_message should not be defined (or should be set to None).

    For more specific instances of user errors, this class can (and should) be inherited \
    by other classes, so that the global reply mechanism remains consistent.
    """

    def __init__(
            self,
            description: str = '',
            reply_message: str | None = None,
            parse_mode: ParseMode = ParseMode.MARKDOWN
    ) -> None:
        """
        :param description: (short) description of the error to be used for internal purposes, \
        such as documentation or generation of logs.

        :param reply_message: message to be sent to the user (intended for frontend error handling)

        :param parse_mode: parse mode of the reply (markdown, html, etc.). Markdown by default.
        """
        self.description = description
        self.reply_message = reply_message
        self.parse_mode = parse_mode
        super().__init__(self.description)

    def __str__(self):
        return self.description

