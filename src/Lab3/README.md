# Lab3 : Computational Process Management

Group Name: Oreo

List of group members:  Liang Ziyi (202320060) , Liu Yixuan (202320063)

Variant description: 2 - Multiple-dispatch

## Synopsis

- The library should support multiple-dispatch on positional, optional and named arguments.
- The library should be well documented.
- Use unit tests with several multi-methods, which works with standard Python types and user-defined types
- Demonstrate how it works with inheritances and multiple inheritances.

## Contribution summary for each group member

Liang Ziyi completed the data structure design and code writing. 

Liu Yixuan completed data testing and documentation.

## Explanation of taken design decisions and analysis

We designed the multi-dispatch library using decorators and multi-method classes. It can supports multiple-dispatch on positional, optional and named arguments. In the file of test,we test the "foo" function by using named arguments ,and we can use "foo" function regardless of number of parameters. Also,inheritance is demonstrated by inheriting and extending class decorators.

## Result

Run results of the entire test file.

![fff50999efab6f92c09ef6545ea721e](https://user-images.githubusercontent.com/39373318/121800410-2dac6200-cc64-11eb-8bbd-9b9597d3833b.png)


## Conclusion

This experiment can be annotated with @multimethod to assign functions according to different types of arguments and pass optional, positional and named parameter tests. Multiple-dispatch is initially achieved.

