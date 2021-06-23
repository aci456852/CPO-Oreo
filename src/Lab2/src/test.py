
from src.Lab2.src.mathematical_expression import MathExpression
# from src.mathematical_expression import MathExpression
from hypothesis import given
import hypothesis.strategies as st
import pytest

@given(b=st.lists(st.integers()))
def test_add(b):
    a = []  # The code is to limit the input data
    flag = 0
    for i in b:
        if flag == 0:
            if i >= 0  and i < 10000:
                a.append(i)
                flag = 1
        else:
            if i < 10000 and i > -10000:
                a.append(i)
    if len(a) > 0:
        expression = ''
        expression += str(a[0])
        sum = a[0]
        for i in a[1:]:
            sum += i
            if i >= 0:
                expression += '+'
            expression += str(i)

        print(expression)
        s = MathExpression(expression)
        s.convert_string()
        res = s.evaluate()
        assert res == sum

@given(b=st.lists(st.integers()))
def test_sub(b):
    a = []  # The code is to limit the input data
    flag = 0
    for i in b:
        if flag == 0:
            if i >= 0  and i < 10000:
                a.append(i)
                flag = 1
        else:
            if i < 10000 and i > -10000:
                a.append(i)
    if len(a) > 0:
        expression = ''
        expression += str(a[0])
        sum = a[0]
        for i in a[1:]:
            if i < 0:
                sum += i
            if i >= 0:
                sum -= i
                expression += '-'
            expression += str(i)
        print(expression)
        s = MathExpression(expression)
        s.convert_string()
        res = s.evaluate()
        assert res == sum

@given(b=st.lists(st.integers()))
def test_mul(b):
    a = []  # The code is to limit the input data
    for i in b:
        if i >= 0 and i < 100:
            a.append(i)
    if len(a) > 0:
        expression = ''
        expression += str(a[0])
        sum = a[0]
        for i in a[1:]:
            sum *= i
            if i >= 0:
                expression += '*'
            expression += str(i)
        print(expression)
        s = MathExpression(expression)
        s.convert_string()
        res = s.evaluate()
        assert res == sum

@given(b=st.lists(st.integers()))
def test_div(b):
    a = []  # The code is to limit the input data
    for i in b:
        if i > 0 and i < 100:
            a.append(i)
    if len(a) > 0:
        expression = ''
        expression += str(a[0])
        sum = a[0]
        for i in a[1:]:
            sum /= i
            if i > 0:
                expression += '/'
            expression += str(i)
        print(expression)
        s = MathExpression(expression)
        s.convert_string()
        res = s.evaluate()
        assert res == sum

def test_mix1():
    expression = '((2+3)*6/(1+4))-1'
    str = MathExpression(expression)
    str.convert_string()
    res = str.evaluate()
    assert res == 5

def test_mix2():
    expression = 'sin(0)+cos(0)-pow(2,3)'
    str = MathExpression(expression)
    str.convert_string()
    res = str.evaluate()
    assert res == -7

def test_specific_function1():
    expression = '(a+1)*(b+3)+func(7)'
    str = MathExpression(expression)
    str.convert_string()
    res = str.evaluate(func=lambda x:pow(x,2)+1,a=2,b=5)
    assert res == 74

def test_specific_function2():
    expression = 'func(2,1,0)*a/b'
    str = MathExpression(expression)
    str.convert_string()
    res = str.evaluate(func=lambda x,y,z: x+y+z,a = 10,b = 2)
    assert res == 15

def test_error1():
    expression = 'a*b+c/d'
    str = MathExpression(expression)
    str.convert_string()
    with pytest.raises(ZeroDivisionError):
        str.evaluate(a=1, b=2, c=3, d=0)

def test_dataflow():
    expression = '(4-1)*(pow(2,3)+cos(0))'
    str = MathExpression(expression)
    str.convert_string()
    str.Visualization()

