from time import time
from random import seed, randint

from compbot.schemas.roll_schemas import RollStr, RollResult


def roll(roll_str: RollStr) -> RollResult:
    """
    Rolls dice according to the specifications of a roll string.

    :param roll_str: roll string containing number of dice, faces and a modifier
    :return: result object containing dice rolled, modifier and result
    """
    seed(time())
    rolled_dice = [randint(1, roll_str.num_faces) for _ in range(roll_str.num_dice)]
    return RollResult(rolled_dice=rolled_dice, modifier=roll_str.modifier)

