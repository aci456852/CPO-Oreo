"""
Variants: 1(a)
In this program, we have completed three functions, realize the interpretation of expressions, calculate mathematical expressions, and convert mathematical expressions into dataflow graphs.
"""

from math import *

op = ['+', '-', '*', '/', '(', ')', ',']
op_level = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

class MyStack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.items[-1]

    def reverse(self):
        return self.items.reverse()

    def size(self):
        return len(self.items)

# This module will report an error when the input mathematical expression is wrong.
def Runtime_Error(f):
    def check(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError:
            print('ValueError! Please check the input!')
    return check

class MathExpression(object):
    def __init__(self, exp=''):
        self.exp = exp
        self.nodes = []
        self.values = dict()

    def convert_string(self):
        str = self.exp.replace(' ', '')
        op_stack = MyStack()
        temp_s = ''
        flag1, flag2 = 0, 0
        for index, j in enumerate(str):
            if flag2 == 1:
                if j not in op:
                    temp_s += j
                    continue
                else:
                    if len(temp_s) == 1:
                        self.nodes.append(temp_s)
                    else:
                        op_stack.push(temp_s)
                    flag2 = 0

            # Storage constant
            if j.isdigit() or j == '.':
                if flag1 == 0:
                    self.nodes.append(j)
                    flag1 = 1
                else:
                    self.nodes[-1] = self.nodes[-1] + j
                continue
            flag1 = 0

            if j.isalpha():
                temp_s = j
                flag2 = 1
                continue

            if j == ',':
                continue

            if op_stack.size() == 0:
                op_stack.push(j)
                continue

            if j == '(':
                op_stack.push(j)
                continue

            if j == ')':
                while op_stack.top() != '(':
                    self.nodes.append(op_stack.pop())
                op_stack.pop()
                if (op_stack.size() != 0) and (op_stack.top() not in op):
                    self.nodes.append(op_stack.pop())
                continue

            while (op_stack.size() != 0) and op_level[op_stack.top()] >= op_level[j]:
                self.nodes.append(op_stack.pop())

            op_stack.push(j)

        if flag2 == 1:
            self.nodes.append(temp_s)

        while op_stack.size() != 0:
            self.nodes.append(op_stack.pop())

    @Runtime_Error
    def Visualization(self):
        res = []
        res.append('digraph dataflow {')

        for index, n in enumerate(self.nodes):
            res.append('n_{}[label="{}"];'.format(index, n))

        count = len(self.nodes)

        node_stack = MyStack()
        for index, n in enumerate(self.nodes):
            if n in ['sin', 'cos', 'tan','abs']:
                node1 = node_stack.pop()
                res.append('{} -> n_{};'.format(node1, index))
                node_stack.push('n_{}'.format(index))
            elif n in op or n in ['log', 'pow']:
                node1 = node_stack.pop()
                node2 = node_stack.pop()
                res.append('{} -> n_{};'.format(node1, index))
                res.append('{} -> n_{};'.format(node2, index))
                node_stack.push('n_{}'.format(index))
            elif n not in self.values.keys():
                node_stack.push('n_{}'.format(index))
            elif len(n) == 1:
                res.append('n_{}[label="{}"];'.format(count, self.values[n]))
                res.append('n_{} -> n_{};'.format(count, index))
                count += 1
                node_stack.push('n_{}'.format(index))
            else:
                func = self.values[n]
                arg_nums = func.__code__.co_argcount
                for k in range(arg_nums):
                    node1 = node_stack.pop()
                    res.append('{} -> n_{};'.format(node1, index))
                node_stack.push('n_{}'.format(index))
        res.append('}')
        file = open('../graph/math_expression.dot','w')
        file.write("\n".join(res))
        print("\n".join(res))

    @Runtime_Error
    def evaluate(self, **kwargs):
        node_stack = MyStack()
        self.values = kwargs
        for n in self.nodes:
            if n == 'sin':
                node_stack.push(sin(node_stack.pop()))
            elif n == 'cos':
                node_stack.push(cos(node_stack.pop()))
            elif n == 'tan':
                node_stack.push(tan(node_stack.pop()))
            elif n == 'abs':
                node_stack.push(abs(node_stack.pop()))
            elif n in ['+', '-', '*', '/', 'log', 'pow']:
                right = node_stack.pop()
                left = node_stack.pop()
                if n == '+':
                    node_stack.push(left + right)
                elif n == '-':
                    node_stack.push(left - right)
                elif n == '*':
                    node_stack.push(left * right)
                elif n == '/':
                    node_stack.push(left / right)
                elif n == 'log':
                    node_stack.push(log(left, right))
                elif n == 'pow':
                    node_stack.push(pow(left, right))
            elif n not in self.values.keys():
                node_stack.push(float(n))
            elif len(n) == 1:
                node_stack.push(self.values[n])
            else:
                func = self.values[n]
                arg_nums = func.__code__.co_argcount
                args = dict()
                for k in range(arg_nums):
                    args[k] = node_stack.pop()
                res_temp = func(*args.values())
                node_stack.push(res_temp)
        return node_stack.pop()
