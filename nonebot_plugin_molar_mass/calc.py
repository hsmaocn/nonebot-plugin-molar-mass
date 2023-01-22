from typing import Union

from .lexer import lexer
from .parser import parser


def calc(chemical: str) -> Union[int, float]:
    result: Union[int, float] = parser.parse(lexer.lex(chemical)).eval()
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result
