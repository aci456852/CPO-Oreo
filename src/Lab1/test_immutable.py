
from src.Lab1.immutable import *
from hypothesis import given
import hypothesis.strategies as st
import pytest
import collections

def test_get_value():
    od = OrderedDict()
    assert get_value(od, 5) == 5
    assert get_value(od, 24) == 4

def test_add():
    od = OrderedDict()
    od = add(od, 2, 1)
    assert find(od, 2) == 1
    assert to_dict(od) == {2: 1}
    od = add(od, 4, 2)
    assert find(od, 4) ==2
    od = add(od, "A", 3)
    assert find(od, "A") == 3
    od = add(od, True, 4)
    assert find(od, True) == 4
    od = add(od, False, 5)
    assert find(od, False) == 5
    od = add(od, 3.14, 6)
    assert find(od, 3.14) == 6

def test_remove():
    od = OrderedDict()
    dict1 = {1: 2, 2: 4, 3: 6}
    od = from_dict(od, dict1)
    remove(od, 1)
    with pytest.raises(Exception):  # Exception detection
        remove(od, 5)
    dict2 = {2: 4, 3: 6}
    assert to_dict(od) == dict2

def test_remove_key_set():
    od = OrderedDict()
    assert od.key_set == []
    od = from_dict(od, {1: 2, 2: 4, 3: 6})
    assert od.key_set == [1, 2, 3]
    od = remove_key_set(od, 1)
    assert od.key_set == [2, 3]

def test_from_dict():
    od = OrderedDict()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    from_dict(od, dict)
    assert find(od, 4) == 8
    assert find(od, 3) == 6

def test_to_dict():
    od = OrderedDict()
    od = add(od, 1, 2)
    od = add(od, 2, 4)
    od = add(od, 3, 6)
    od = add(od, 4, 8)
    to_dict(od)
    assert to_dict(od) == {1: 2, 2: 4, 3: 6, 4: 8}

def test_get_size():
    od = OrderedDict()
    assert get_size(od) == 0
    od = add(od, 1, 2)
    assert get_size(od) == 1
    od = add(od, 14, 2)
    assert get_size(od) == 2

def test_from_list():
    test_data = [
        [],
        ['a', 'b', 'c'],
        ['0', '11', '111'],
        [1, 2, 3],
        [None]
    ]
    for e in test_data:
        od = OrderedDict()
        od = from_list(od, e)
        assert to_list(od) == e

def test_to_list():
    od = OrderedDict()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    od = from_dict(od, dict)
    assert to_list(od) == [2, 4, 6, 8]

def test_find_iseven():
    od = OrderedDict()
    od = from_list(od, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert to_list(od) == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert find_iseven(od) == [2, 4, 6.0, 8]

def test_filter_iseven():
    od = OrderedDict()
    od = from_list(od, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert to_list(od) == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert filter_iseven(od) == ['a', 1, 3.14, 'b', 5, 'c', 7]

def test_map():
    dict1 = {1: 2, 2: 4}
    dict2 = {1: '2', 2: '4'}
    od = OrderedDict()
    od = from_dict(od, dict1)
    assert map(od, str) == dict2

def test_reduce():
    od = OrderedDict()
    assert reduce(od, lambda st, e: st + e, 0) == 0
    dict1 = {1: 2, 2: 4}
    od1 = OrderedDict()
    od1 = from_dict(od1, dict1)
    assert reduce(od1, lambda st, e: st + e, 0) == 6

def test_od_collision():
    od = OrderedDict()
    od = add(od, 1, 7)
    od = add(od, 11, 777)
    assert get_value(od, 1) == get_value(od, 11)  # check input two keys have the same od
    assert find(od, 1) == 7  # check that data inside your structure store well
    assert find(od, 11) == 777

def test_iter():
    dict1 = {1: 2, 2: 4, 3: 6, 4: 8}
    od = OrderedDict()
    od = from_dict(od, dict1)
    tmp = {}
    for e in od:
        tmp[e.key] = e.value
    assert to_dict(od) == tmp
    i = iter(OrderedDict())
    pytest.raises(StopIteration, lambda: next(i))

# e·a = a·e = acollision
@given(a=st.lists(st.integers()))
def test_monoid_identity(a):
    od = OrderedDict()
    od_a = OrderedDict()
    od_a = from_list(od_a, a)
    assert mconcat(mempty(od), od_a) == od_a
    assert mconcat(od_a, mempty(od)) == od_a

# (a·b)·c = a·(b·c)
@given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
def test_monoid_associativity(a, b, c):
    od_a = OrderedDict()
    od_b = OrderedDict()
    od_c = OrderedDict()
    od_a = from_list(od_a, a)
    od_b = from_list(od_b, b)
    od_c = from_list(od_c, c)
    # (a·b)·c
    a_b = mconcat(od_a, od_b)
    ab_c = mconcat(a_b, od_c)

    od_a1 = OrderedDict()
    od_b1 = OrderedDict()
    od_c1 = OrderedDict()
    od_a1 = from_list(od_a1, a)
    od_b1 = from_list(od_b1, b)
    od_c1 = from_list(od_c1, c)
    # a·(b·c)
    b_c = mconcat(od_b1, od_c1)
    a_bc = mconcat(od_a1, b_c)

    assert id(ab_c) != id(a_bc)  # address is not same
    assert to_list(ab_c) == to_list(a_bc)  # value is same

@given(st.lists(st.integers()))
def test_from_list_to_list_equality(a):
    od = OrderedDict()
    od = from_list(od, a)
    b = to_list(od)
    assert a == b

@given(st.lists(st.integers()))
def test_python_len_and_list_size_equality(a):
    od = OrderedDict()
    od = from_list(od, a)
    assert get_size(od) == len(a)

@given(st.lists(st.integers()))
def test_from_list(a):
    od = OrderedDict()
    od = from_list(od, a)
    assert to_list(od) == a

def test_iter():
    x = [1, 2, 3]
    od = OrderedDict()
    od = from_list(od, x)
    tmp = []
    try:
        get_next = iterator(od)
        while True:
            tmp.append(get_next())
    except StopIteration:
        pass
    assert x == tmp
    assert to_list(od) == tmp

    get_next = iterator(None)
    assert get_next() == False
