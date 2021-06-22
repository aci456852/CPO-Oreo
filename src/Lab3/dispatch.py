from src.Lab3.multiMethod import *


@multimethod(int, float)
@multimethod(str, float)
def bar(a, b=20) -> float:
    if type(a) != float:
        a = float(a)
    return a + b



@multimethod(int)
@multimethod(int, int)
def foo(a, b=2) -> int:
    return a + b


@multimethod(float, float)
def foo(a, b) -> float:
    return a - b


@multimethod(str, str)
def foo(a, b) -> str:
    return a + b


@multimethod(dict, dict)
def foo(a, b) -> dict:
    res = {**a, **b}
    return res


@multimethod(str)
@multimethod(str, int)
def foo(a, b=10) -> str:
    c = str(b)
    return a + c


@multimethod(float)
@multimethod(float, int)
@multimethod(float, int, str)
def foo(a, b=20, c='30') -> float:
    d = int(c)
    return (a + b + d)/3
