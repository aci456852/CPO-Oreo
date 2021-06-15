
from src.Lab1.mutable import *
from hypothesis import given
import hypothesis.strategies as st
import pytest


def test_get_value():
    hash = HashMap()
    assert hash.get_value(5) == 5
    assert hash.get_value(24) == 4

def test_add():
    hash = HashMap()
    hash.add(2, 6)
    assert hash.find(2) == 6
    assert hash.to_dict() == {2: 6}
    hash.add(4, 5)
    assert hash.find(4) == 5
    hash.add(1, 5)
    assert hash.find(1) == 5
    hash.add("A", 1)  # 3. Remove key type restriction
    assert hash.find("A") == 1
    hash.add(True, 3)
    assert hash.find(True) == 3
    hash.add(False, 9)
    assert hash.find(False) == 9
    hash.add(3.14, 1)
    assert hash.find(3.14) == 1

def test_remove():
    hash = HashMap()
    dict1 = {1: 2, 2: 4, 3: 6}
    hash.from_dict(dict1)
    hash.remove(1)
    with pytest.raises(Exception):  # Exception detection
        hash.remove(5)
    dict2 = {2: 4, 3: 6}
    assert hash.to_dict() == dict2

def test_get():
    hash = HashMap()
    hash.add(1, 5)
    hash.add(2, 10)
    hash.add(4, 5)
    hash.add(5, 10)
    assert hash.find(1) == 5
    assert hash.find(2) == 10
    assert hash.find(4) == 5
    assert hash.find(5) == 10

def test_remove_key_set():
    hash = HashMap()
    assert hash.key_set == []
    hash.from_dict({1: 2, 2: 4, 3: 6})
    assert hash.key_set == [1, 2, 3]
    hash.remove_key_set(1)
    assert hash.key_set == [2, 3]

def test_from_dict():
    hash = HashMap()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    hash.from_dict(dict)
    assert hash.find(4) == 8
    assert hash.find(3) == 6

def test_to_dict():
    hash = HashMap()
    hash.add(1, 2)
    hash.add(2, 4)
    hash.add(3, 6)
    hash.add(4, 8)
    hash.to_dict()
    assert hash.to_dict() == {1: 2, 2: 4, 3: 6, 4: 8}

def test_get_size():
    hash = HashMap()
    assert hash.get_size() == 0
    hash.add(1, 2)
    assert hash.get_size() == 1
    hash.add(14, 2)
    assert hash.get_size() == 2
    hash.add(1, 3)  # test for same key, new value alter the old one
    assert hash.get_size() == 2

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
        hash.from_list(e)
        assert hash.to_list() == e

def test_to_list():
    hash = HashMap()
    dict = {1: 2, 2: 4, 3: 6, 4: 8}
    hash.from_dict(dict)
    assert  hash.to_list() == [2, 4, 6, 8]

def test_find_iseven():
    hash = HashMap()
    hash.from_list(['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert hash.to_list() == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert hash.find_iseven() == [2, 4, 6.0, 8]

def test_filter_iseven():
    hash = HashMap()
    hash.from_list(['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
    assert hash.to_list() == ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8]
    assert hash.filter_iseven() == ['a', 1, 3.14, 'b', 5, 'c', 7]

def test_map():
    dict1 = {1: 2, 2: 4}
    dict2 = {1: '2', 2: '4'}
    hash = HashMap()
    hash.from_dict(dict1)
    assert hash.map(str) == dict2

def test_reduce():
    hash = HashMap()
    assert hash.reduce(lambda st, e: st + e, 0) == 0
    dict1 = {1: 2, 2: 4}
    hash1 = HashMap()
    hash1.from_dict(dict1)
    assert hash1.reduce(lambda st, e: st + e, 0) == 6

def test_hash_collision():
    hash = HashMap()
    hash.add(1, 7)
    hash.add(11, 777)
    assert hash.get_value(1) == hash.get_value(11)  # check input two keys have the same hash
    assert hash.find(1) == 7  # check that data inside your structure store well
    assert hash.find(11) == 777

def test_iter():
    dict1 = {1: 2, 2: 4, 3: 6, 4: 8}
    table = HashMap()
    table.from_dict(dict1)
    tmp = {}
    for e in table:
        tmp[e.key] = e.value
    assert table.to_dict(), tmp
    i = iter(HashMap())
    pytest.raises(StopIteration, lambda: next(i))

# e·a = a·e = a
@given(a=st.lists(st.integers()))
def test_monoid_identity(a):
    hash = HashMap()
    hash_a = HashMap()
    hash_a.from_list(a)
    assert hash.mconcat(hash.mempty(), hash_a) == hash_a
    assert hash.mconcat(hash_a, hash.mempty()) == hash_a

# (a·b)·c = a·(b·c)
@given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
def test_monoid_associativity(a, b, c):
    hash = HashMap()
    hash_a = HashMap()
    hash_b = HashMap()
    hash_c = HashMap()
    hash_a.from_list(a)
    hash_b.from_list(b)
    hash_c.from_list(c)
    # (a·b)·c
    a_b = hash.mconcat(hash_a, hash_b)
    ab_c = hash.mconcat(a_b, hash_c)

    hash1 = HashMap()
    hash_a1 = HashMap()
    hash_b1 = HashMap()
    hash_c1 = HashMap()
    hash_a1.from_list(a)
    hash_b1.from_list(b)
    hash_c1.from_list(c)
    # a·(b·c)
    b_c = hash1.mconcat(hash_b1, hash_c1)
    a_bc = hash1.mconcat(hash_a1, b_c)

    assert id(ab_c) != id(a_bc)  # address is not same
    assert ab_c.to_list() == a_bc.to_list()  # value is same

@given(st.lists(st.integers()))
def test_from_list_to_list_equality(a):
    hash = HashMap()
    hash.from_list(a)
    b = hash.to_list()
    assert a == b

@given(st.lists(st.integers()))
def test_python_len_and_list_size_equality(a):
    hash = HashMap()
    hash.from_list(a)
    assert hash.get_size() == len(a)

@given(st.lists(st.integers()))
def test_from_list(a):
    hash = HashMap()
    hash.from_list(a)
    assert hash.to_list() == a