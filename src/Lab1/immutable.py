# coding=utf-8
"""
Author: Liang Ziyi
Date: 2021/3/20
Title: Dictionary based on hash-map (immutable)
"""
from typing import List, Tuple

class Node(object):
    def __init__(self, key=None, value=None, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return "Node [key=" + self.key + ",value=" + self.value + "]"

class HashMap(object):

    def __init__(self, dict=None) -> None:
        self.key_set = []
        self.size = 10
        self.data = [Node() for _ in range(10)]

        # Initialize dict
        if dict is not None:
            self.from_dict(self, dict)


# get hash value
def get_value(hash: HashMap, key: int) -> int:
    hash_value = key % hash.size
    return hash_value


# insert key-value pairs into hash map
def add(hash: HashMap, key: object, value: int) -> HashMap:
    # copy structure
    new_hash = HashMap()
    new_hash.size = hash.size
    for x in range(len(hash.key_set)):
        new_hash.key_set.append(hash.key_set[x])
    for x in range(len(hash.data)):
        new_hash.data[x] = hash.data[x]

    if type(key) == str:  # change key's type for remove key type restriction --str
        key = ord(key)
    if type(key) == bool:  # change key's type for remove key type restriction --bool
        if key == True:
            key = 1
        else:
            key = 0
    if type(key) == float:  # change key's type for remove key type restriction --float
        key = int(key)

    hash_value = get_value(new_hash, key)
    if new_hash is None:
        new_hash = HashMap()
    if new_hash.data[hash_value].key is None:
        new_hash.data[hash_value].value = value
        new_hash.data[hash_value].key = key
        new_hash.key_set.append(key)
    else:
        temp = Node(key, value)
        new_hash.key_set.append(key)
        p = new_hash.data[hash_value]
        while p.next is not None:
            p = p.next
        p.next = temp
    return new_hash


# remove element in hash map by key
def remove(hash, key) -> HashMap:
    # Add tests for exceptions
    if key is None:
        raise Exception("remove not existence key!")

    # copy structure
    new_hash = HashMap()
    new_hash.size = hash.size
    for x in range(len(hash.key_set)):
        new_hash.key_set.append(hash.key_set[x])
    for x in range(len(hash.data)):
        new_hash.data[x] = hash.data[x]

    if new_hash is None:
        raise Exception("new_hash is None!")
    hash_value = get_value(new_hash, key)
    if new_hash.data[hash_value].value is None:
        raise Exception('No valid key value was found')
    else:
        p = new_hash.data[hash_value]
        if key == p.key:
            if p.next is None:
                p.key = None
                p.value = None
            else:
                temp = p.next
                p.key = temp.key
                p.value = temp.value
                p.next = temp.next
            remove_key_set(new_hash, key)
            return new_hash
        else:
            while p is not None:
                if p.key == key:
                    temp = p.next
                    p.next = temp.next
                    remove_key_set(new_hash, key)
                    return new_hash
                else:
                    p = p.next
    raise Exception('No valid key value was found')


# find element in hash map by key
def find(hash: HashMap, key: int) -> object:
    if type(key) == str:  # change key's type for remove key type restriction --str
        key = ord(key)
    if type(key) == bool:  # change key's type for remove key type restriction --bool
        if key == True:
            key = 1
        else:
            key = 0
    if type(key) == float:  # change key's type for remove key type restriction --float
        key = int(key)

    if hash.key_set is None:
        return None
    i = 0
    while i < hash.size:
        if hash.data[i].key is None:
            i += 1
            continue
        else:
            p = hash.data[i]
            while p is not None:
                if p.key == key:
                    return p.value
                p = p.next
            i += 1
    raise Exception("can not find the key")


def remove_key_set(hash: HashMap, key: int) -> HashMap:
    # Add tests for exceptions
    if key is None:
        raise Exception("remove not existence key!")

    # copy structure
    new_hash = HashMap()
    new_hash.size = hash.size
    for x in range(len(hash.key_set)):
        new_hash.key_set.append(hash.key_set[x])
    for x in range(len(hash.data)):
        new_hash.data[x] = hash.data[x]

    for i, k in enumerate(new_hash.key_set):
        if key == k:
            arr = new_hash.key_set
            del arr[i]
            return new_hash

    raise Exception("can not find the key")


def from_dict(hash: HashMap, dict: dict) -> HashMap:
    new_hash = HashMap()
    new_hash.size = hash.size
    for x in range(len(hash.key_set)):
        new_hash.key_set.append(hash.key_set[x])
    for x in range(len(hash.data)):
        new_hash.data[x] = hash.data[x]

    for key, value in dict.items():
        new_hash = add(new_hash, key, value)

    return new_hash

# transfer hash map into dict
def to_dict(hash: HashMap) -> {}:
    myDict = {}
    if hash is None:
        return myDict
    else:
        i = 0
        while i < hash.size:
            if hash.data[i].value is None:
                i += 1
                continue
            else:
                p = hash.data[i]
                while p is not None:
                    myDict[p.key] = p.value
                    p = p.next
                i += 1
    return myDict


# element number in hash map
def get_size(hash: HashMap) -> int:
    sum = 0
    i = 0
    while i < hash.size:
        if hash.data[i].value is None:
            i += 1
            continue
        else:
            p = hash.data[i]
            while p is not None:
                sum += 1
                p = p.next
            i += 1
    return sum


# transfer hash map into list type
def to_list(hash: HashMap) -> List:
    list = []
    if hash is None:
        return list
    for i, key in enumerate(hash.key_set):
        list.append(find(hash, key))
    return list


# add element from list type
def from_list(hash: HashMap, list: List) -> HashMap:
    new_hash = HashMap()
    new_hash.size = hash.size
    for x in range(len(hash.key_set)):
        new_hash.key_set.append(hash.key_set[x])
    for x in range(len(hash.data)):
        new_hash.data[x] = hash.data[x]

    for key, value in enumerate(list):
        new_hash = add(new_hash, key, value)
    return new_hash

# find element with even value in hash map.
def find_iseven(hash: HashMap) -> HashMap:
    list = to_list(hash)
    my_list = []
    for value in range(len(list)):
        if type(list[value]) is int or type(list[value]) is float:
            if list[value] % 2 == 0:
                my_list.append(list[value])
    return my_list


# filter element with even value in hash map.
def filter_iseven(hash: HashMap) -> List:
    list = to_list(hash)
    for value in list:
        if type(value) is int or type(value) is float:
            if value % 2 == 0:
                list.remove(value)
    return list


# map element value in hash map with f
def map(hash: HashMap, f: type) -> dict:
    dict = to_dict(hash)
    for key in hash.key_set:
        value = f(find(hash, key))
        dict[key] = value
    return dict


#  build a return value by specific functions(f)
def reduce(hash: HashMap, f, initial_state):
    state = initial_state
    for key in hash.key_set:
        value = find(hash, key)
        state = f(state, value)
    return state


def mempty(hash) -> None:
    return None


def mconcat(a: HashMap, b: HashMap) -> HashMap:
    if a is None:
        return b
    if b is None:
        return a
    for key in b.key_set:
        value = find(b, key)
        a = add(a, key, value)
    return a


# iterator
def iterator(hash: HashMap) -> object:
    if hash is not None:
        res = []
        list = to_list(hash)
        for i in list:
            res.append(i)
        a = iter(res)
    else:
        a = None

    def get_next():
        if a is None:
            return False
        else:
            return next(a)

    return get_next
