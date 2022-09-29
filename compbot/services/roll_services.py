from time import time
from random import seed, randint
from re import compile

from telegram.constants import ParseMode

from compbot.utils.exceptions import UserError


ROLL_REGEX = r'\s*(\d+)\s*d\s*(\d+)(\s*[+-]\s*\d+)?\s*'


def parse_roll_str(roll_str: str) -> tuple[int, int, int]:
    """
    Validates a roll string and extracts number of dice, number of faces and modifier from it.

    :param roll_str: roll string of the format "AdB [+/- C]", where A is the number of dice,
    B is the number of faces and C is the optional roll modifier.

    :return: tuple of the format (A,B,C) as above, with C defaulted to zero if not provided.

    :raise ValueError: raised if string does not match required format.
    """
    # Create regex mask to match strings like "2d6" or "2d6 + 5"
    roll_pattern = compile(ROLL_REGEX)
    # Verify match
    match = roll_pattern.match(roll_str)
    if not match:
        raise UserError(
            description='User did not provide roll string as argument',
            reply_message='A jogada deve ser, por exemplo, da forma <code>1d6</code> ou <code>1d4+5</code>',
            parse_mode=ParseMode.HTML
        )
    # Extract values
    num_dice, num_faces, modifier = match.groups()
    # Check modifier
    if modifier is None:
        modifier = 0
    elif '+' in modifier:
        _, modifier = modifier.split('+')
    elif '-' in modifier:
        _, modifier = modifier.split('-')
        modifier = -int(modifier)
    # Return tuple
    return int(num_dice), int(num_faces), int(modifier)


def roll(num_dice: int, num_faces: int, modifier: int = 0) -> int:
    """
    Rolls dice.

    :param num_dice: number of dice to be rolled.
    :param num_faces: number of faces (possible values) of each die.
    :param  modifier: modifier to be added to the rolled results (defaults to zero).
    :return: sum of results of rolled dice added to the modifier
    """
    seed(time())
    total_rolled = sum([randint(1, num_faces) for _ in range(num_dice)])
    return total_rolled + modifier

