from src.Lab3.multiMethod import *


@multimethod(int)
@multimethod(int, int)
def foo(a, b=2):
    return a + b


@multimethod(float, float)
def foo(a, b):
    return a - b


@multimethod(str, str)
def foo(a, b):
    return a + b


@multimethod(dict, dict)
def foo(a, b):
    res = {**a, **b}
    return res


@multimethod(str)
@multimethod(str, int)
def foo(a, b=10):
    c = str(b)
    return a + c



@multimethod(float)
@multimethod(float, int)
@multimethod(float, int, str)
def foo(a, b=20, c='30'):
    d = int(c)
    return (a + b + d)/3