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

![a3dc210d5c42fe153b677005a6b3422](https://user-images.githubusercontent.com/73821262/113508086-a1553300-9580-11eb-9691-02484df2dc77.png)

The functions of **mutable dict** are as follows：

+ get_value

  We get the position of the known number in the hash map by integer remainder method.

  ![get value](https://user-images.githubusercontent.com/73821262/111927801-d5036980-8a66-11eb-990e-5a1e638d00aa.png)

+ add

  First, we get the position in the hash map through the key value, and then add it to the hash map. We solve the key value conflict through the linked list. At the same time, you need to increase the size of the table

  ![add](https://user-images.githubusercontent.com/73821262/111927827-e3ea1c00-8a66-11eb-9cf5-0baed4590f17.png)

+ remove

  Similarly, the key value is used to find its position in the hash map, search in the linked list of the position, and judge whether it exists. If it exists, delete it and return true. If it does not exist, return false.

  ![remove](https://user-images.githubusercontent.com/73821262/111927862-ecdaed80-8a66-11eb-94c3-35a3b77acadc.png)

+ find

  We find element in hash map by key.

  ![get](https://user-images.githubusercontent.com/73821262/111927874-f49a9200-8a66-11eb-9849-e12a691a7435.png)

+ remove_key_set

  We remove element in hash map by key. At the same time, we increase the size of the table.

  ![remove_key_set](https://user-images.githubusercontent.com/73821262/111927896-fb290980-8a66-11eb-9859-8bd7a879d3a9.png)

+ from_dict

  Convert dictionary to hash map.

  ![from_dict](https://user-images.githubusercontent.com/73821262/111927905-00865400-8a67-11eb-9244-f4130e00d1b2.png)

+ to_dict

  First, an empty dictionary is created, and then the elements in the HashMap are stored in the dictionary in the form of key value pairs.

  ![to_dict](https://user-images.githubusercontent.com/73821262/111927918-07ad6200-8a67-11eb-94b9-e3f64533942b.png)

+ get_size

  We can get the size of hash map by this function.

  ![get_size](https://user-images.githubusercontent.com/73821262/111927922-0bd97f80-8a67-11eb-8db5-715902c79c50.png)

+ to_list

  transfer hash map into list type.

  ![to_list](https://user-images.githubusercontent.com/73821262/111927929-109e3380-8a67-11eb-8eaf-2f02a53afba4.png)

+ from_list

  This function realizes the function of adding data in the form of array to the dictionary.

  ![from_list](https://user-images.githubusercontent.com/73821262/111927934-1431ba80-8a67-11eb-9683-0edef6bad17b.png)

+ find_iseven

  We can use this function to determine whether there is an even number in the hash map. If there is, we will return the result set in the form of list.

  ![find_iseven](https://user-images.githubusercontent.com/73821262/111927942-1ac03200-8a67-11eb-88fd-4796ecd93500.png)

+ filter_iseven

  Traverse hash map, and then judge whether it has even number. If there is even number, delete it. If there is no even number, ignore it. Finally, return the processed result set.

  ![filter_iseven](https://user-images.githubusercontent.com/73821262/111927949-20b61300-8a67-11eb-8330-119991c7d55c.png)

+ map

  This function can map the element values in hash map with f.

  ![map](https://user-images.githubusercontent.com/73821262/111927958-24e23080-8a67-11eb-8ec0-7dfd549b8be6.png)

+ reduce

  build a return value by specific functions(f)

  ![reduce](https://user-images.githubusercontent.com/73821262/111927963-2ad81180-8a67-11eb-8fdc-aecf56458146.png)

+ iter

  This function is used to access an iteratable sequence.

  ![iter](https://user-images.githubusercontent.com/73821262/111927971-2f042f00-8a67-11eb-8a8d-11588e928f7d.png)

+ mempty

  This function returns None.

+ mconcat

  Judge whether one of the two incoming objects is none, and return none. If both objects are not empty, return the union of them.

  ![monoid_identity](https://user-images.githubusercontent.com/73821262/111927980-375c6a00-8a67-11eb-8586-798418c3d70d.png)

  ![monoid_associativity](https://user-images.githubusercontent.com/73821262/111927987-3c211e00-8a67-11eb-8e14-34d95dbb3f62.png)

##### Immutable

![9f98cd35fcb835dd52a2df9a79c2772](https://user-images.githubusercontent.com/73821262/113508074-90a4bd00-9580-11eb-86ba-edac5e4d5723.png)

+ get_value

  Return value by key.

  ![getvalue](https://user-images.githubusercontent.com/73821262/111928013-4a6f3a00-8a67-11eb-8a75-98a3477e4407.png)

+ add

  insert key-value pairs into hash map

  ![add](https://user-images.githubusercontent.com/73821262/111928020-4e02c100-8a67-11eb-8e32-87b9b2e3c944.png)

+ remove

  remove element in hash map by key.

  ![remove](https://user-images.githubusercontent.com/73821262/111928022-522ede80-8a67-11eb-9709-cb9f48f52f62.png)

+ find

  find element in hash map by key.

  ![get](https://user-images.githubusercontent.com/73821262/111928024-55c26580-8a67-11eb-9c5a-f952b6d24af5.png)

+ remove_key_set

  Delete a key in hash map.

  ![remove key set](https://user-images.githubusercontent.com/73821262/111928034-5b1fb000-8a67-11eb-9226-a93cf84b6b96.png)

+ from_dict

  Convert dictionary to hash map.

  ![from dict](https://user-images.githubusercontent.com/73821262/111928042-5f4bcd80-8a67-11eb-9b2c-e491e98f7eb4.png)

+ to_dict

  transfer hash map into dict

  ![to dict](https://user-images.githubusercontent.com/73821262/111928047-6541ae80-8a67-11eb-8f61-29bb14fe3837.png)

+ get_size

  get the number of element in hash map

  ![get size](https://user-images.githubusercontent.com/73821262/111928054-6b378f80-8a67-11eb-9629-730230ed707e.png)

+ to_list

  transfer hash map into list type.

  ![to list](https://user-images.githubusercontent.com/73821262/111928061-6ffc4380-8a67-11eb-9e22-ae4a889c51c2.png)

+ from_list

  add element from list type.

  ![from list](https://user-images.githubusercontent.com/73821262/111928074-768abb00-8a67-11eb-9c9c-4fea8e9dd20c.png)

+ find_iseven

  find element with even value in hash map.

  ![find iseven](https://user-images.githubusercontent.com/73821262/111928086-7db1c900-8a67-11eb-87d8-2422a5cbc79e.png)

+ filter_iseven

  filter element with even value in hash map.

  ![filter iseven](https://user-images.githubusercontent.com/73821262/111928092-84d8d700-8a67-11eb-9400-c337623b540f.png)

+ map

  map element value in hash map with f

  ![map](https://user-images.githubusercontent.com/73821262/111928095-8a362180-8a67-11eb-9096-25c032b72a4d.png)

+ reduce

  build a return value by specific functions(f)

  ![reduce](https://user-images.githubusercontent.com/73821262/111928101-8f936c00-8a67-11eb-980b-be7bd4b3d5cb.png)

+ mempty

  return a none value.

+ mconcat

  Judge whether one of the two incoming objects is none, and return none. If both objects are not empty, return the union of them.

  ![monoid identity](https://user-images.githubusercontent.com/73821262/111928110-9621e380-8a67-11eb-9f81-579eb474b4a9.png)

  ![monoid_associativity](https://user-images.githubusercontent.com/73821262/111928114-991cd400-8a67-11eb-8d79-e4e152b82802.png)

+ iterator

  This function is used to access an iteratable sequence.

  ![iter](https://user-images.githubusercontent.com/73821262/111928123-9e7a1e80-8a67-11eb-9ed5-09ecd43c0a14.png)

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

## Test
test_immutably.py and test_mutable.py implemented pytest test.

![test_mutable.py](https://user-images.githubusercontent.com/73821262/122053191-1b275980-ce19-11eb-846b-e4f189308484.png)

![test_immutably.py](https://user-images.githubusercontent.com/73821262/122053217-21b5d100-ce19-11eb-968e-fcba91c30a86.png)
