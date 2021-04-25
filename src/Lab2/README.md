# Lab2:Basic Model of Computational

Group Name: Oreo

List of group members:  Liang Ziyi , Liu Yixuan

Variant description: 1(a)-Mathematical expression. Parse input string in a tree (node - functions; leaf - 		constant) and reduce it in a result (from leaves to root)

## synopsis

Input language is a sting like "a + 2 - sin(-0.3)*(b - c)". We should parse the input string in a tree and reduce it in a result. We should first transform the input into "a 2+ 0.3 - sin b c - \* -". Then we need to build a tree according to the expression. We also need to write a program to calculate the result of the mathematical expression. We can also use the graphviz module to complete the dataflow graph.

## Contribution summary for each group member

Liu Yixuan completed the data structure design and code writing. 

Liang Ziyi completed data testing and documentation.

## Explanation of taken design decisions and analysis

First, we need to complete the conversion of mathematical expressions and set up two stacks, one to store operators and the other to store operands. Read the string in sequence, and put it directly into the stack when encountering an operand. When encountering an operator, first check the level of the element on the top of the stack. If the current operation level is higher than the operation level on the top of the stack, it will be directly put on the stack. The top element is popped from the stack. The main idea of converting an expression into a tree is to use it as a leaf node if the node element is an operand, and as a parent node if it is an operator.

## Work demonstration

```python
    def test_add(self):
        expression = '1+2+3+4+5'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res,15)
```

![image-20210425141541542](C:%5CUsers%5CMSI-NB%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210425141541542.png)

```python
    def test_error1(self):
        expression = 'a*b+c/d'
        str = MathExpression(expression)
        str.convert_string()
        with self.assertRaises(ZeroDivisionError):
            str.evaluate(a=1, b=2, c=3, d=0)
```

![image-20210425141737922](C:%5CUsers%5CMSI-NB%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210425141737922.png)

```python
    def test_dataflow(self):
        expression = '(4-1)*(pow(2,3)+cos(0))'
        str = MathExpression(expression)
        str.convert_string()
        str.Visualization()
```

![image-20210425141900695](C:%5CUsers%5CMSI-NB%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210425141900695.png)

![math_expression](E:%5Cgitworkspace%5CCPO-Oreo%5Csrc%5CLab2%5Cgraph%5Cmath_expression.png)

Run results of the entire test file.

![image-20210425145544068](C:%5CUsers%5CMSI-NB%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210425145544068.png)

## Conclusion

This experiment completed the conversion and calculation of mathematical expressions. This program can calculate common operators including +,-,*,/,sin,cos,pow,log,abs, and completed the visualization of the expression.