from telegram.constants import ParseMode

from compbot.utils.exceptions import UserError


class NoRollStr(UserError):

    def __init__(self):
        super().__init__(
            description='User did not provide roll string as argument',
            reply_message='Por favor, especifique qual jogada tenho que fazer.\n\n'
                          '<b>Exemplos:</b> <code>1d6</code> ou <code>1d4+5</code>',
            parse_mode=ParseMode.HTML
        )


class InvalidRollStr(UserError):

    def __init__(self):
        super().__init__(
            description='User did not provide roll string as argument',
            reply_message='A jogada deve ser, por exemplo, da forma <code>1d6</code> ou <code>1d4+5</code>',
            parse_mode=ParseMode.HTML
        )
