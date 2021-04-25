import unittest
from src.Lab2.src.mathematical_expression import MathExpression


class MyTestCase(unittest.TestCase):
    def test_add(self):
        expression = '1+2+3+4+5'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res,15)

    def test_sub(self):
        expression = '10-2-2-2'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res,4)

    def test_mul(self):
        expression = '10*2*2'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res, 40)

    def test_div(self):
        expression = '22/2'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res, 11)

    def test_mix1(self):
        expression = '((2+3)*6/(1+4))-1'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res, 5)

    def test_mix2(self):
        expression = 'sin(0)+cos(0)-pow(2,3)'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate()
        self.assertEqual(res, -7)

    def test_specific_function1(self):
        expression = '(a+1)*(b+3)+func(7)'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate(func=lambda x:pow(x,2)+1,a=2,b=5)
        self.assertEqual(res, 74)

    def test_specific_function2(self):
        expression = 'func(2,1,0)*a/b'
        str = MathExpression(expression)
        str.convert_string()
        res = str.evaluate(func=lambda x,y,z: x+y+z,a = 10,b = 2)
        self.assertEqual(res, 15)

    def test_error1(self):
        expression = 'a*b+c/d'
        str = MathExpression(expression)
        str.convert_string()
        with self.assertRaises(ZeroDivisionError):
            str.evaluate(a=1, b=2, c=3, d=0)

    def test_dataflow(self):
        expression = '(4-1)*(pow(2,3)+cos(0))'
        str = MathExpression(expression)
        str.convert_string()
        str.Visualization()

if __name__ == '__main__':
    unittest.main()
