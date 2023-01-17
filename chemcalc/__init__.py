from typing import Union

from .lexer import lexer
from .parser import parser, Expr


def calc(code: str) -> Union[int, float]:
    result: Union[int, float] = parser.parse(lexer.lex(code)).eval()
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result
