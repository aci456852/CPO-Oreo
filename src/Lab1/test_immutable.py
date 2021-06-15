
from src.Lab1.immutable import *
from hypothesis import given
import hypothesis.strategies as st
import pytest

def test_get_value():
    hash = HashMap()
    assert get_value(hash, 5) == 5
    assert get_value(hash, 24) == 4

def test_add():
    hash = HashMap()
    hash = add(hash, 2, 1)
    assert find(hash, 2) == 1
    assert to_dict(hash) == {2: 1}
    hash = add(hash, 4, 2)
    assert find(hash, 4) ==2
    hash = add(hash, "A", 3)
    assert find(hash, "A") == 3
    hash = add(hash, True, 4)
    assert find(hash, True) == 4
    hash = add(hash, False, 5)
    assert find(hash, False) == 5
    hash = add(hash, 3.14, 6)
    assert find(hash, 3.14) == 6

def test_remove():
    hash = HashMap()
    dict1 = {1: 2, 2: 4, 3: 6}
    hash = from_dict(hash, dict1)
    remove(hash, 1)
    with pytest.raises(Exception):  # Exception detection
        remove(hash, 5)
    dict2 = {2: 4, 3: 6}
    assert to_dict(hash) == dict2

def test_remove_key_set():
    hash = HashMap()
    assert hash.key_set == []
    hash = from_dict(hash, {1: 2, 2: 4, 3: 6})
    assert hash.key_set == [1, 2, 3]
    hash = remove_key_set(hash, 1)
    assert hash.key_set == [2, 3]

def test_from_dict():
    hash = HashMap()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    from_dict(hash, dict)
    assert find(hash, 4) == 8
    assert find(hash, 3) == 6

def test_to_dict():
    hash = HashMap()
    hash = add(hash, 1, 2)
    hash = add(hash, 2, 4)
    hash = add(hash, 3, 6)
    hash = add(hash, 4, 8)
    to_dict(hash)
    assert to_dict(hash) == {1: 2, 2: 4, 3: 6, 4: 8}

def test_get_size():
    hash = HashMap()
    assert get_size(hash) == 0
    hash = add(hash, 1, 2)
    assert get_size(hash) == 1
    hash = add(hash, 14, 2)
    assert get_size(hash) == 2

def test_from_list():
    test_data = [
        [],
        ['a', 'b', 'c'],
        ['0', '11', '111'],
        [1, 2, 3],
        [None]
    ]
    for e in test_data:
        hash = HashMap()
        hash = from_list(hash, e)
        assert to_list(hash) == e

def test_to_list():
    hash = HashMap()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    hash = from_dict(hash, dict)
    assert to_list(hash) == [2, 4, 6, 8]

def test_find_iseven():
    hash = HashMap()
    hash = from_list(hash, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert to_list(hash) == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert find_iseven(hash) == [2, 4, 6.0, 8]

def test_filter_iseven():
    hash = HashMap()
    hash = from_list(hash, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert to_list(hash) == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert filter_iseven(hash) == ['a', 1, 3.14, 'b', 5, 'c', 7]

def test_map():
    dict1 = {1: 2, 2: 4}
    dict2 = {1: '2', 2: '4'}
    hash = HashMap()
    hash = from_dict(hash, dict1)
    assert map(hash, str) == dict2

def test_reduce():
    hash = HashMap()
    assert reduce(hash, lambda st, e: st + e, 0) == 0
    dict1 = {1: 2, 2: 4}
    hash1 = HashMap()
    hash1 = from_dict(hash1, dict1)
    assert reduce(hash1, lambda st, e: st + e, 0) == 6

def test_hash_collision():
    hash = HashMap()
    hash = add(hash, 1, 7)
    hash = add(hash, 11, 777)
    assert get_value(hash, 1) == get_value(hash, 11)  # check input two keys have the same hash
    assert find(hash, 1) == 7  # check that data inside your structure store well
    assert find(hash, 11) == 777

def test_iter():
    dict1 = {1: 2, 2: 4, 3: 6, 4: 8}
    hash = HashMap()
    hash = from_dict(hash, dict1)
    tmp = {}
    for e in hash:
        tmp[e.key] = e.value
    assert to_dict(hash) == tmp
    i = iter(HashMap())
    pytest.raises(StopIteration, lambda: next(i))

# e·a = a·e = acollision
@given(a=st.lists(st.integers()))
def test_monoid_identity(a):
    hash = HashMap()
    hash_a = HashMap()
    hash_a = from_list(hash_a, a)
    assert mconcat(mempty(hash), hash_a) == hash_a
    assert mconcat(hash_a, mempty(hash)) == hash_a

# (a·b)·c = a·(b·c)
@given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
def test_monoid_associativity(a, b, c):
    hash_a = HashMap()
    hash_b = HashMap()
    hash_c = HashMap()
    hash_a = from_list(hash_a, a)
    hash_b = from_list(hash_b, b)
    hash_c = from_list(hash_c, c)
    # (a·b)·c
    a_b = mconcat(hash_a, hash_b)
    ab_c = mconcat(a_b, hash_c)

    hash_a1 = HashMap()
    hash_b1 = HashMap()
    hash_c1 = HashMap()
    hash_a1 = from_list(hash_a1, a)
    hash_b1 = from_list(hash_b1, b)
    hash_c1 = from_list(hash_c1, c)
    # a·(b·c)
    b_c = mconcat(hash_b1, hash_c1)
    a_bc = mconcat(hash_a1, b_c)

    assert id(ab_c) != id(a_bc)  # address is not same
    assert to_list(ab_c) == to_list(a_bc)  # value is same

@given(st.lists(st.integers()))
def test_from_list_to_list_equality(a):
    hash = HashMap()
    hash = from_list(hash, a)
    b = to_list(hash)
    assert a == b

@given(st.lists(st.integers()))
def test_python_len_and_list_size_equality(a):
    hash = HashMap()
    hash = from_list(hash, a)
    assert get_size(hash) == len(a)

@given(st.lists(st.integers()))
def test_from_list(a):
    hash = HashMap()
    hash = from_list(hash, a)
    assert to_list(hash) == a

def test_iter():
    x = [1, 2, 3]
    hash = HashMap()
    hash = from_list(hash, x)
    tmp = []
    try:
        get_next = iterator(hash)
        while True:
            tmp.append(get_next())
    except StopIteration:
        pass
    assert x == tmp
    assert to_list(hash) == tmp

    get_next = iterator(None)
    assert get_next() == False
