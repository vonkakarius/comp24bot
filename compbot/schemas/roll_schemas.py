from re import compile

from compbot.exceptions.roll_exceptions import InvalidRollStr


ROLL_REGEX = r'\s*(\d+)\s*d\s*(\d+)(\s*[+-]\s*\d+)?\s*'


class RollStr(str):

    def __new__(cls, roll_str: str):
        return super().__new__(cls, roll_str)

    def __init__(self, _: str):
        if not self.is_valid():
            raise InvalidRollStr()

    def is_valid(self):
        match = compile(ROLL_REGEX).match(self.__str__())
        return match is not None

    @property
    def num_dice(self) -> int:
        match = compile(ROLL_REGEX).match(self.__str__())
        num_dice, _, _ = match.groups()
        return int(num_dice)

    @property
    def num_faces(self) -> int:
        match = compile(ROLL_REGEX).match(self.__str__())
        _, num_faces, _ = match.groups()
        return int(num_faces)

    @property
    def modifier(self) -> int:
        match = compile(ROLL_REGEX).match(self.__str__())
        _, _, modifier = match.groups()
        # Check modifier
        if modifier is None:
            modifier = 0
        elif '+' in modifier:
            _, modifier = modifier.split('+')
            modifier = int(modifier)
        elif '-' in modifier:
            _, modifier = modifier.split('-')
            modifier = -int(modifier)
        return modifier


class RollResult:

    def __init__(self, rolled_dice: list[int], modifier: int):
        self._rolled_dice = rolled_dice
        self._total = sum(rolled_dice)
        self._modifier = modifier

    @property
    def rolled_dice(self) -> list[int]:
        return self._rolled_dice

    @property
    def total(self) -> int:
        return self._total

    @property
    def modifier(self) -> int:
        return self._modifier

    @property
    def result(self) -> int:
        return self._total + self._modifier

    def __str__(self):
        result_str = ' + '.join([str(result) for result in self._rolled_dice])
        if self._modifier != 0:
            result_str += ' + ' if self._modifier > 0 else ' - '
            result_str += str(abs(self._modifier))
        result_str += f' = {self.result}'
        return result_str
