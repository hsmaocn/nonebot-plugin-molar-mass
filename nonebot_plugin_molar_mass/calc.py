from typing import Union

from .lexer import lexer
from .parser import parser


class CalcException(Exception):
    pass


def calc_molar_mass(chemical: str) -> Union[int, float]:
    """
    Calculates the molar mass of given chemical.
    :raise CalcException: if fails to calculate.
    :param chemical: the chemical to calculate.
    :return: the molar mass.
    """

    try:
        result: Union[int, float] = parser.parse(lexer.lex(chemical)).eval()
    except Exception as e:
        raise CalcException() from e

    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result
