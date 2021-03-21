# Lab1:Different approach for algorithms and data structure implementation

Group Name: Oreo

List of group members:  Liang Ziyi , Liu Yixuan

Variant description:  7-Dictionary based on hash-map (collision resolution: separate chaining）

## synopsis

In this laboratory work, we should develop a library for a specific data structure. Wu should  implement the selected data structure in two way:

+ as a mutable object (interaction with an object should modify it if applicable)
+ as an immutable object (interaction with an object cannot change it).

## Introduction and verification of function realization

##### Mutable

The functions of **mutable dict** are as follows：

+ get_value

  We get the position of the known number in the hash map by integer remainder method.

  ![get_value](./pics/mutable/get value.png)

+ add

  First, we get the position in the hash map through the key value, and then add it to the hash map. We solve the key value conflict through the linked list. At the same time, you need to increase the size of the table

  ![add](./pics/mutable/add.png)

+ remove

  Similarly, the key value is used to find its position in the hash map, search in the linked list of the position, and judge whether it exists. If it exists, delete it and return true. If it does not exist, return false.

  ![remove](./pics/mutable/remove.png)

+ find

  We find element in hash map by key.

  ![find](./pics/mutable/get.png)

+ remove_key_set

  We remove element in hash map by key. At the same time, we increase the size of the table.

  ![remove_key_set](./pics/mutable/remove_key_set.png)

+ from_dict

  Convert dictionary to hash map.

  ![from_dict](./pics/mutable/from_dict.png)

+ to_dict

  First, an empty dictionary is created, and then the elements in the HashMap are stored in the dictionary in the form of key value pairs.

  ![to_dict](./pics/mutable/to_dict.png)

+ get_size

  We can get the size of hash map by this function.

  ![get_size](./pics/mutable/get_size.png)

+ to_list

  transfer hash map into list type.

  ![to_list](./pics/mutable/to_list.png)

+ from_list

  This function realizes the function of adding data in the form of array to the dictionary.

  ![from_list](./pics/mutable/from_list.png)

+ find_iseven

  We can use this function to determine whether there is an even number in the hash map. If there is, we will return the result set in the form of list.

  ![find_iseven](./pics/mutable/find_iseven.png)

+ filter_iseven

  Traverse hash map, and then judge whether it has even number. If there is even number, delete it. If there is no even number, ignore it. Finally, return the processed result set.

  ![filter_iseven](./pics/mutable/filter_iseven.png)

+ map

  This function can map the element values in hash map with f.

  ![map](./pics/mutable/map.png)

+ reduce

  build a return value by specific functions(f)

  ![reduce](./pics/mutable/reduce.png)

+ iter

  This function is used to access an iteratable sequence.

  ![iter](./pics/mutable/iter.png)

+ mempty

  This function returns None.

+ mconcat

  Judge whether one of the two incoming objects is none, and return none. If both objects are not empty, return the union of them.

  ![monoid](./pics/mutable/monoid_identity.png)

  ![monoid](./pics/mutable/monoid_associativity.png)

##### Immutable

+ get_value

  Return value by key.

  ![get_value](./pics/immutable/getvalue.png)

+ add

  insert key-value pairs into hash map

  ![add](./pics/immutable/add.png)

+ remove

  remove element in hash map by key.

  ![remove](./pics/immutable/remove.png)

+ find

  find element in hash map by key.

  ![find](./pics/immutable/get.png)

+ remove_key_set

  Delete a key in hash map.

  ![remove_key_set](./pics/immutable/remove key set.png)

+ from_dict

  Convert dictionary to hash map.

  ![from_dict](./pics/immutable/from dict.png)

+ to_dict

  transfer hash map into dict

  ![to_dict](./pics/immutable/to dict.png)

+ get_size

  get the number of element in hash map

  ![get_size](./pics/immutable/get size.png)

+ to_list

  transfer hash map into list type.

  ![to_list](./pics/immutable/to list.png)

+ from_list

  add element from list type.

  ![from_list](./pics/immutable/from list.png)

+ find_iseven

  find element with even value in hash map.

  ![find_iseven](./pics/immutable/find iseven.png)

+ filter_iseven

  filter element with even value in hash map.

  ![filter_iseven](./pics/immutable/filter iseven.png)

+ map

  map element value in hash map with f

  ![map](./pics/immutable/map.png)

+ reduce

  build a return value by specific functions(f)

  ![reduce](./pics/immutable/reduce.png)

+ mempty

  return a none value.

+ mconcat

  Judge whether one of the two incoming objects is none, and return none. If both objects are not empty, return the union of them.

  ![mconcat](./pics/immutable/monoid identity.png)

  ![mconcat](./pics/immutable/monoid_associativity.png)

+ iterator

  This function is used to access an iteratable sequence.

  ![iter](./pics/immutable/iter.png)

## Contribution summary for each group member

Liang Ziyi completed the data structure design and code writing. 

Liu Yixuan completed data testing and documentation.

## Explanation of taken design decisions and analysis

Firstly, the dictionary is implemented by hash table, and the conflict is solved by separate chaining, and the data structure is designed. Secondly, it is divided into mutable and immutable object for coding and testing. Compare mutable and immutable implementation, we can find out mutable program use built-in functions，and immutable program's built-in function is only initialization, and the related usage is written outside, which is an independent method. Thirdly, when writing test cases, it is not difficult to find that the logic code of the two is consistent, and the only difference is the function calls.

## Work demonstration

For mutable dict, we define a HashMap class, we can use it in such way.

```python
from Lab1.mutable import *
hash = HashMap()
hash.from_dict({1:17,2:15,3:18})
print(hash.to_dict())
```

For test class, we use pycharm to develop it . if you want to test a function of mutable tree, you can click **play** icon to run a test for a function.

## Conclusion

In this experiment, we completed the design and implementation of the dictionary based on hash map (changeable and immutable). The mutable object can be changed after it is created, and the address will not change at the same time. The opposite is true for immutable objects. After the object is created, it cannot be changed. Once the address is changed, the variable points to a new object.

We realize the functions of adding, deleting, modifying, checking, size, structure conversion and many more. This experiment deepened our understanding of python and data structure.
