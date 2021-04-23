# coding=utf-8
"""
Author: Liang Ziyi
Date: 2021/3/20
Title: Dictionary based on hash-map (immutable_test)
"""

import unittest
from src.Lab1.immutable import *
from hypothesis import given
import hypothesis.strategies as st


class TestImmutableList(unittest.TestCase):
    def test_get_value(self):
        hash = HashMap()
        self.assertEqual(get_value(hash, 5), 5)
        self.assertEqual(get_value(hash, 24), 4)

    def test_add(self):
        hash = HashMap()
        hash = add(hash, 2, 1)
        self.assertEqual(find(hash, 2), 1)
        self.assertEqual(to_dict(hash), {2: 1})
        hash = add(hash, 4, 2)
        self.assertEqual(find(hash, 4), 2)
        hash = add(hash, "A", 3)
        self.assertEqual(find(hash, "A"), 3)
        hash = add(hash, True, 4)
        self.assertEqual(find(hash, True), 4)
        hash = add(hash, False, 5)
        self.assertEqual(find(hash, False), 5)
        hash = add(hash, 3.14, 6)
        self.assertEqual(find(hash, 3.14), 6)

    def test_remove(self):
        hash = HashMap()
        dict1 = {1: 2, 2: 4, 3: 6}
        from_dict(hash, dict1)
        remove(hash, 1)
        dict2 = {2: 4, 3: 6}
        self.assertEqual(to_dict(hash), dict2)

    def test_remove_key_set(self):
        hash = HashMap()
        self.assertEqual(hash.key_set, [])
        hash = from_dict(hash, {1: 2, 2: 4, 3: 6})
        self.assertEqual(hash.key_set, [1, 2, 3])
        hash = remove_key_set(hash, 1)
        self.assertEqual(hash.key_set, [2, 3])

    def test_from_dict(self):
        hash = HashMap()
        dict = {1: 2, 2: 4, 3: 6, 4: 8}
        from_dict(hash, dict)
        self.assertEqual(find(hash, 4), 8)
        self.assertEqual(find(hash, 3), 6)

    def test_to_dict(self):
        hash = HashMap()
        hash = add(hash, 1, 2)
        hash = add(hash, 2, 4)
        hash = add(hash, 3, 6)
        hash = add(hash, 4, 8)
        to_dict(hash)
        self.assertEqual(to_dict(hash), {1: 2, 2: 4, 3: 6, 4: 8})

    def test_get_size(self):
        hash = HashMap()
        self.assertEqual(get_size(hash), 0)
        hash = add(hash, 1, 2)
        self.assertEqual(get_size(hash), 1)
        hash = add(hash, 14, 2)
        self.assertEqual(get_size(hash), 2)

    def test_from_list(self):
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
            self.assertEqual(to_list(hash), e)

    def test_to_list(self):
        hash = HashMap()
        dict = {1: 2, 2: 4, 3: 6, 4: 8}
        hash = from_dict(hash, dict)
        self.assertEqual(to_list(hash), [2, 4, 6, 8])

    def test_find_iseven(self):
        hash = HashMap()
        hash = from_list(hash, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
        self.assertEqual(to_list(hash), ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
        self.assertEqual(find_iseven(hash), [2, 4, 6.0, 8])

    def test_filter_iseven(self):
        hash = HashMap()
        hash = from_list(hash, ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
        self.assertEqual(to_list(hash), ['a', 1, 2, 3.14, 'b', 4, 5, 'c', 6.0, 7, 8])
        self.assertEqual(filter_iseven(hash), ['a', 1, 3.14, 'b', 5, 'c', 7])

    def test_map(self):
        dict1 = {1: 2, 2: 4}
        dict2 = {1: '2', 2: '4'}
        hash = HashMap()
        hash = from_dict(hash, dict1)
        self.assertEqual(map(hash, str), dict2)

    def test_reduce(self):
        hash = HashMap()
        self.assertEqual(reduce(hash, lambda st, e: st + e, 0), 0)
        dict1 = {1: 2, 2: 4}
        hash1 = HashMap()
        hash1 = from_dict(hash1, dict1)
        self.assertEqual(reduce(hash1, lambda st, e: st + e, 0), 6)

    def test_hash_collision(self):
        hash1 = HashMap()
        hash2 = HashMap()
        hash = add(hash1, 1, 777)
        hash = add(hash2, 11, 777)
        self.assertEqual(get_value(hash1, 1), get_value(hash2, 11))

    def test_iter(self):
        dict1 = {1: 2, 2: 4, 3: 6, 4: 8}
        hash = HashMap()
        hash = from_dict(hash, dict1)
        tmp = {}
        for e in hash:
            tmp[e.key] = e.value
        self.assertEqual(to_dict(hash), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))

    @given(a=st.lists(st.integers()))
    def test_monoid_identity(self, a):
        hash = HashMap()
        hash_a = HashMap()
        hash_a = from_list(hash_a, a)
        self.assertEqual(mconcat(mempty(hash), hash_a), hash_a)
        self.assertEqual(mconcat(hash_a, mempty(hash)), hash_a)

    def test_monoid_associativity(self):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        hash_a = add(hash_a, 1, 2)
        hash_b = add(hash_b, 2, 3)
        hash_c = add(hash_c, 3, 6)
        # (a·b)·c
        a_b = mconcat(hash_a, hash_b)
        ab_c = mconcat(a_b, hash_c)

        hash_a1 = HashMap()
        hash_b1 = HashMap()
        hash_c1 = HashMap()
        hash_a1 = add(hash_a1, 1, 2)
        hash_b1 = add(hash_b1, 2, 3)
        hash_c1 = add(hash_c1, 3, 6)
        # a·(b·c)
        b_c = mconcat(hash_b1, hash_c1)
        a_bc = mconcat(hash_a1, b_c)

        assert id(ab_c) != id(a_bc)  # address is not same
        self.assertEqual(to_list(ab_c), to_list(a_bc))  # value is same

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        hash = HashMap()
        hash = from_list(hash, a)
        b = to_list(hash)
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        hash = HashMap()
        hash = from_list(hash, a)
        self.assertEqual(get_size(hash), len(a))

    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        hash = HashMap()
        hash = from_list(hash, a)
        self.assertEqual(to_list(hash), a)

    def test_iter(self):
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
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(hash), tmp)

        get_next = iterator(None)
        self.assertEqual(get_next(), False)


if __name__ == '__main__':
    unittest.main()