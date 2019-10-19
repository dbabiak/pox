from string import ascii_letters, digits
from typing import *
from dataclasses import dataclass


class PoxError(Exception):
    pass


@dataclass(frozen=True)
class Token:
    char: int
    lexeme: str


def peek(s: str, i: int) -> Optional[str]:
    return s[i] if i < len(s) else None


class LeftParen(Token):
    pass


class RightParen(Token):
    pass


class LeftBrace(Token):
    pass


class RightBrace(Token):
    pass


class Comma(Token):
    pass


class Dot(Token):
    pass


class Minus(Token):
    pass


class Plus(Token):
    pass


class SemiColon(Token):
    pass


class Slash(Token):
    pass


class Star(Token):
    pass


class Bang(Token):
    pass


class BangEqual(Token):
    pass


class Equal(Token):
    pass


class EqualEqual(Token):
    pass


class Greater(Token):
    pass


class GreaterEqual(Token):
    pass


class Less(Token):
    pass


class LessEqual(Token):
    pass


class Identifier(Token):
    pass


class WhiteSpace(Token):
    pass


class And(Token):
    pass


class Class(Token):
    pass


class Else(Token):
    pass


class Nope(Token):
    pass


class Troo(Token):
    pass


class Fun(Token):
    pass


class For(Token):
    pass


class If(Token):
    pass


class Null(Token):
    pass


class Or(Token):
    pass


class Print(Token):
    pass


class Return(Token):
    pass


class Super(Token):
    pass


class This(Token):
    pass


class Var(Token):
    pass


class While(Token):
    pass


class String(Token):
    pass


class Number(Token):
    pass


class EOF(Token):
    pass




def _left_paren(src: str, i: int) -> Optional[LeftParen]:
    if src[i] == "(":
        return LeftParen(char=i, lexeme=src[i])


def _right_paren(src: str, i: int) -> Optional[RightParen]:
    if src[i] == ")":
        return RightParen(char=i, lexeme=src[i])


def _left_brace(src: str, i: int) -> Optional[LeftBrace]:
    if src[i] == "{":
        return LeftBrace(char=i, lexeme=src[i])


def _right_brace(src: str, i: int) -> Optional[RightBrace]:
    if src[i] == "}":
        return RightBrace(char=i, lexeme=src[i])


def _comma(src: str, i: int) -> Optional[Comma]:
    if src[i] == ",":
        return Comma(char=i, lexeme=src[i])


def _dot(src: str, i: int) -> Optional[Dot]:
    if src[i] == ".":
        return Dot(char=i, lexeme=src[i])


def _minus(src: str, i: int) -> Optional[Minus]:
    if src[i] == "-":
        return Minus(char=i, lexeme=src[i])


def _plus(src: str, i: int) -> Optional[Plus]:
    if src[i] == "+":
        return Plus(char=i, lexeme=src[i])


def _semicolon(src: str, i: int) -> Optional[SemiColon]:
    if src[i] == ";":
        return SemiColon(char=i, lexeme=src[i])


def _slash(src: str, i: int) -> Optional[Slash]:
    if src[i] == "/":
        return Slash(char=i, lexeme=src[i])


def _star(src: str, i: int) -> Optional[Star]:
    if src[i] == "*":
        return Star(char=i, lexeme=src[i])


def _bang(src: str, i: int) -> Optional[Bang]:
    if src[i] == "!":
        return Bang(char=i, lexeme=src[i])


def _bang_equal(src: str, i: int) -> Optional[BangEqual]:
    if src[i : i + 1] == "!=":
        return BangEqual(char=i, lexeme=src[i : i + 1])


def _equal(src: str, i: int) -> Optional[Equal]:
    if src[i] == "=":
        return Equal(char=i, lexeme=src[i])


def _equalequal(src: str, i: int) -> Optional[EqualEqual]:
    if src[i : i + 1] == "==":
        return EqualEqual(char=i, lexeme=src[i : i + 1])


def _greater(src: str, i: int) -> Optional[Greater]:
    if src[i] == ">":
        return Greater(char=i, lexeme=src[i : i + 1])


def _greaterequal(src: str, i: int) -> Optional[GreaterEqual]:
    if src[i : i + 1] == ">=":
        return GreaterEqual(char=i, lexeme=src[i : i + 1])


def _less(src: str, i: int) -> Optional[Less]:
    if src[i] == "<":
        return Less(char=i, lexeme=src[i : i + 1])


def _lessequal(src: str, i: int) -> Optional[LessEqual]:
    if src[i : i + 1] == "<=":
        return LessEqual(char=i, lexeme=src[i : i + 1])


def _identifier(src: str, i: int) -> Optional[Identifier]:
    if src[i] in ascii_letters:
        j = i + 1
        while j < len(src) and src[j] in (ascii_letters + digits):
            j += 1
        return Identifier(char=i, lexeme=src[i:j])


def _string(src: str, i: int) -> Optional[String]:
    if src[i] == '"':
        j = i + 1
        while j < len(src) and src[j] != '"':
            j += 1
        return String(char=i, lexeme=src[i : j + 1])


def _number(src: str, i: int) -> Optional[Number]:
    if src[i] in digits:
        j = i + 1
        while j < len(src) and src[j] in digits:
            j += 1

        # do we have a decimal? if yes, keep counting
        if j < len(src) and src[j] == ".":
            j += 1
            while j < len(src) and src[j] in digits:
                j += 1

        return Number(char=i, lexeme=src[i:j])


def _whitespace(src: str, i: int) -> Optional[WhiteSpace]:
    if src[i] == " ":
        j = i + 1
        while j < len(src) and src[j] == " ":
            j += 1
        return WhiteSpace(char=i, lexeme=src[i:j])


def _and(src: str, i: int) -> Optional[And]:
    if src[i : i + 3] == "and":
        return And(char=i, lexeme=src[i : i + 3])


def _class(src: str, i: int) -> Optional[Class]:
    if src[i : i + 5] == "class":
        return Class(char=i, lexeme=src[i : i + 5])


def _else(src: str, i: int) -> Optional[Else]:
    if src[i : i + 4] == "else":
        return Else(char=i, lexeme=src[i : i + 4])


def _nope(src: str, i: int) -> Optional[Nope]:
    if src[i : i + 4] == "nope":
        return Nope(char=i, lexeme=src[i : i + 4])


def _fun(src: str, i: int) -> Optional[Fun]:
    if src[i : i + 3] == "fun":
        return Fun(char=i, lexeme=src[i : i + 3])


def _for(src: str, i: int) -> Optional[For]:
    if src[i : i + 3] == "for":
        return For(char=i, lexeme=src[i : i + 3])


def _if(src: str, i: int) -> Optional[If]:
    if src[i : i + 2] == "if":
        return If(char=i, lexeme=src[i : i + 2])


def _null(src: str, i: int) -> Optional[Null]:
    if src[i : i + 4] == "null":
        return Null(char=i, lexeme=src[i : i + 4])


def _or(src: str, i: int) -> Optional[Or]:
    if src[i : i + 2] == "or":
        return Or(char=i, lexeme=src[i : i + 2])


def _print(src: str, i: int) -> Optional[Print]:
    if src[i : i + 5] == "print":
        return Print(char=i, lexeme=src[i : i + 5])


def _return(src: str, i: int) -> Optional[Return]:
    if src[i : i + 6] == "return":
        return Return(char=i, lexeme=src[i : i + 6])


def _super(src: str, i: int) -> Optional[Super]:
    if src[i : i + 5] == "super":
        return Super(char=i, lexeme=src[i : i + 5])


def _this(src: str, i: int) -> Optional[This]:
    if src[i : i + 4] == "this":
        return This(char=i, lexeme=src[i : i + 4])


def _troo(src: str, i: int) -> Optional[Troo]:
    if src[i : i + 4] == "troo":
        return Troo(char=i, lexeme=src[i : i + 4])


def _var(src: str, i: int) -> Optional[Var]:
    if src[i : i + 2] == "var":
        return Var(char=i, lexeme=src[i : i + 2])


def _while(src: str, i: int) -> Optional[While]:
    if src[i : i + 5] == "while":
        return While(char=i, lexeme=src[i : i + 5])


_tokenizers: Sequence[Callable[[str, int], Optional[Token]]] = (
    _left_paren,
    _right_paren,
    _left_brace,
    _right_brace,
    _comma,
    _dot,
    _minus,
    _plus,
    _semicolon,
    _slash,
    _star,
    _bang,
    _bang_equal,
    _equal,
    _equalequal,
    _greater,
    _greaterequal,
    _less,
    _lessequal,
    _string,
    _number,
    _whitespace,
    _and,
    _class,
    _else,
    _nope,
    _fun,
    _for,
    _if,
    _null,
    _or,
    _print,
    _return,
    _super,
    _this,
    _troo,
    _var,
    _while,
    _identifier,
)


def _next_token(src: str, i) -> Optional[Token]:
    for f in _tokenizers:
        token = f(src, i)
        if token:
            return token


def tokenize(src: str) -> List[Token]:
    i = 0
    tokens = []
    while i < len(src):
        token = _next_token(src, i)
        if token is None:
            raise PoxError(f"wtf i: {i} context: {src[i-40:i]}")
        tokens.append(token)
        i += len(token.lexeme)
    return tokens
