# coding=utf-8
"""
Author: Liang Ziyi
Date: 2021/3/20
Title: Dictionary based on od-map (immutable)
"""
from typing import List, Tuple, Union, Optional
from typing import TypeVar
import collections

T = TypeVar('T', int, str, bytes, bool)


class Node(object):
    def __init__(self, key=None, value=None, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return "Node [key=" + self.key + ",value=" + self.value + "]"

class OrderedDict(collections.OrderedDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)

    def __init__(self) -> None:
        self.key_set: List[int] = []
        self.size = 10
        self.data = [Node() for _ in range(10)]


# get od value
def get_value(od: OrderedDict, key: T) -> int:
    od_value = key % od.size
    return od_value


# insert key-value pairs into od map
def add(od: OrderedDict, key: T, value: int) -> OrderedDict:
    # copy structure
    new_od = OrderedDict()
    new_od.size = od.size
    for x in range(len(od.key_set)):
        new_od.key_set.append(od.key_set[x])
    for x in range(len(od.data)):
        new_od.data[x] = od.data[x]

    if type(key) == str:  # change key's type for remove key type restriction --str
        key = ord(key)
    if type(key) == bool:  # change key's type for remove key type restriction --bool
        if key == True:
            key = 1
        else:
            key = 0
    if type(key) == float:  # change key's type for remove key type restriction --float
        key = int(key)

    od_value = get_value(new_od, key)
    if new_od is None:
        new_od = OrderedDict()
    if new_od.data[od_value].key is None:
        new_od.data[od_value].value = value
        new_od.data[od_value].key = key
        new_od.key_set.append(key)
    else:
        temp = Node(key, value)
        new_od.key_set.append(key)
        p = new_od.data[od_value]
        while p.next is not None:
            p = p.next
        p.next = temp
    return new_od


# remove element in od map by key
def remove(od: OrderedDict, key: T) -> OrderedDict:
    # Add tests for exceptions
    if key is None:
        raise Exception("remove not existence key!")

    # copy structure
    new_od = OrderedDict()
    new_od.size = od.size
    for x in range(len(od.key_set)):
        new_od.key_set.append(od.key_set[x])
    for x in range(len(od.data)):
        new_od.data[x] = od.data[x]

    if new_od is None:
        raise Exception("new_od is None!")
    od_value = get_value(new_od, key)
    if new_od.data[od_value].value is None:
        raise Exception('No valid key value was found')
    else:
        p = new_od.data[od_value]
        if key == p.key:
            if p.next is None:
                p.key = None
                p.value = None
            else:
                temp = p.next
                p.key = temp.key
                p.value = temp.value
                p.next = temp.next
            remove_key_set(new_od, key)
            return new_od
        else:
            while p is not None:
                if p.key == key:
                    temp = p.next
                    p.next = temp.next
                    remove_key_set(new_od, key)
                    return new_od
                else:
                    p = p.next
    raise Exception('No valid key value was found')


# find element in od map by key
def find(od: OrderedDict, key: T) -> object:
    if type(key) == str:  # change key's type for remove key type restriction --str
        key = ord(key)
    if type(key) == bool:  # change key's type for remove key type restriction --bool
        if key == True:
            key = 1
        else:
            key = 0
    if type(key) == float:  # change key's type for remove key type restriction --float
        key = int(key)

    if od.key_set is None:
        return None
    i = 0
    while i < od.size:
        if od.data[i].key is None:
            i += 1
            continue
        else:
            p = od.data[i]
            while p is not None:
                if p.key == key:
                    return p.value
                p = p.next
            i += 1
    raise Exception("can not find the key")


def remove_key_set(od: OrderedDict, key: T) -> OrderedDict:
    # Add tests for exceptions
    if key is None:
        raise Exception("remove not existence key!")

    # copy structure
    new_od = OrderedDict()
    new_od.size = od.size
    for x in range(len(od.key_set)):
        new_od.key_set.append(od.key_set[x])
    for x in range(len(od.data)):
        new_od.data[x] = od.data[x]

    for i, k in enumerate(new_od.key_set):
        if key == k:
            arr = new_od.key_set
            del arr[i]
            return new_od

    raise Exception("can not find the key")


def from_dict(od: OrderedDict, dict: Optional[dict]) -> OrderedDict:
    new_od = OrderedDict()
    new_od.size = od.size
    for x in range(len(od.key_set)):
        new_od.key_set.append(od.key_set[x])
    for x in range(len(od.data)):
        new_od.data[x] = od.data[x]

    for key, value in dict.items():
        new_od = add(new_od, key, value)

    return new_od

# transfer od map into dict
def to_dict(od: OrderedDict) -> {}:
    myDict = {}
    if od is None:
        return myDict
    else:
        i = 0
        while i < od.size:
            if od.data[i].value is None:
                i += 1
                continue
            else:
                p = od.data[i]
                while p is not None:
                    myDict[p.key] = p.value
                    p = p.next
                i += 1
    return myDict


# element number in od map
def get_size(od: OrderedDict) -> int:
    sum = 0
    i = 0
    while i < od.size:
        if od.data[i].value is None:
            i += 1
            continue
        else:
            p = od.data[i]
            while p is not None:
                sum += 1
                p = p.next
            i += 1
    return sum


# transfer od map into list type
def to_list(od: OrderedDict) -> List:
    list = []
    if od is None:
        return list
    for i, key in enumerate(od.key_set):
        list.append(find(od, key))
    return list


# add element from list type
def from_list(od: OrderedDict, list: List) -> OrderedDict:
    new_od = OrderedDict()
    new_od.size = od.size
    for x in range(len(od.key_set)):
        new_od.key_set.append(od.key_set[x])
    for x in range(len(od.data)):
        new_od.data[x] = od.data[x]

    for key, value in enumerate(list):
        new_od = add(new_od, key, value)
    return new_od

# find element with even value in od map.
def find_iseven(od: OrderedDict) -> OrderedDict:
    list = to_list(od)
    my_list = []
    for value in range(len(list)):
        if type(list[value]) is int or type(list[value]) is float:
            if list[value] % 2 == 0:
                my_list.append(list[value])
    return my_list


# filter element with even value in od map.
def filter_iseven(od: OrderedDict) -> List:
    list = to_list(od)
    for value in list:
        if type(value) is int or type(value) is float:
            if value % 2 == 0:
                list.remove(value)
    return list


# map element value in od map with f
def map(od: OrderedDict, f: type) -> dict:
    dict = to_dict(od)
    for key in od.key_set:
        value = f(find(od, key))
        dict[key] = value
    return dict


#  build a return value by specific functions(f)
def reduce(od: OrderedDict, f, initial_state):
    state = initial_state
    for key in od.key_set:
        value = find(od, key)
        state = f(state, value)
    return state


def mempty(od) -> None:
    return None


def mconcat(a: OrderedDict, b: OrderedDict) -> OrderedDict:
    if a is None:
        return b
    if b is None:
        return a
    for key in b.key_set:
        value = find(b, key)
        a = add(a, key, value)
    return a


# iterator
def iterator(od: OrderedDict) -> object:
    if od is not None:
        res = []
        list = to_list(od)
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
