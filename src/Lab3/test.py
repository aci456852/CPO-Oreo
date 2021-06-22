from src.Lab3.dispatch import *
from src.Lab3.inheritance import *
import pytest


# 1.support for different types
def test_type():
    assert foo(1, 2) == 3
    assert foo(1.0, 1.0) == 0.0
    assert foo('1', 10) == '110'
    assert foo('abc', 'd') == 'abcd'
    assert foo(dict(first_name='Ziyi'), dict(last_name='Liang')) == {'first_name': 'Ziyi', 'last_name': 'Liang'}

# 2.Optional and named parameters
def test_optional():
    assert foo('1') == '110'
    assert foo('11', 0) == '110'
    assert foo(10.0, 40, '10') == 20
    assert foo(10.0) == 20.0
    assert foo(10.0, 2) == 14

# 3.support for named argumants
def test_named_object():
    assert foo(a=1, b=2) == 3
    assert foo(a='1', b=10) == '110'
    assert bar(a=1, b=10.5) == 11.5
    assert bar(a='1', b=10.5) == 11.5

# 4.inherit
def test_inherit():
    assert bar_A(1, 3) == bar_B(1, 3)
    assert bar_B(2, 4) == bar_C(2, 4)

