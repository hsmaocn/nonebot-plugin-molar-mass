import rply
from rply.token import BaseBox
from elements import ELEMENTS


class Expr(BaseBox):
    def eval(self) -> int:
        raise NotImplementedError()


class IntegerExpr(Expr):
    def __init__(self, expr: Expr, count: int):
        self.expr = expr
        self.val = count

    def eval(self) -> int:
        return self.expr.eval() * self.val


class Element(Expr):
    def __init__(self, ele: str):
        self.ele = ele

    def eval(self) -> int:
        if self.ele not in ELEMENTS:
            raise NameError('Cannot find element ' + self.ele)
        return ELEMENTS[self.ele]


class BinaryExpr(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> int:
        return self.left.eval() + self.right.eval()


lg = rply.LexerGenerator()

lg.ignore(r'\s+')
lg.add('INTEGER', r'\d+')
lg.add('ELEMENT', '[A-Z][a-z]?[a-z]?')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')

pg = rply.ParserGenerator([
    'INTEGER', 'ELEMENT', 'OPEN_PARENS', 'CLOSE_PARENS'
])


@pg.production('expr : ele')
@pg.production('expr : paren')
def _(p):
    return p[0]


@pg.production('expr : ele expr')
@pg.production('expr : paren expr')
def _(p):
    return BinaryExpr(p[0], p[1])


@pg.production('paren : OPEN_PARENS expr CLOSE_PARENS')
def _(p):
    return p[1]


@pg.production('paren : OPEN_PARENS expr CLOSE_PARENS INTEGER')
def _(p):
    return IntegerExpr(p[1], int(p[3].getstr()))


@pg.production('ele : ELEMENT')
def _(p):
    return Element(p[0].getstr())


@pg.production('ele : ELEMENT INTEGER')
def _(p):
    return IntegerExpr(Element(p[0].getstr()), int(p[1].getstr()))


parser = pg.build()
lexer = lg.build()


def parse(code: str) -> int:
    return parser.parse(lexer.lex(code)).eval()
