import unittest
from calculator import Calculator

VALID_EXPRESSIONS_DICT = {
    '5 2 /': 2,
    '3 7 *': 21,
    '5 2 %': 1,
    '4 7 + 2 *': 22,
    '1 2 3 +': 5,
    '2 3 * 11 14 * +': 160,
    '1 2 + 3 * 4 5 + +': 18,
    '1 2 + 3 * 4 + 1 2 *': 2,
    '1 2 + 3 * 4 +': 13,
    '1 2 + 3 * 4 + * - + / %': 13,
    '1 2 + 3 * 4 + *': 13,
    '1 2 + 3 * 4 + - * * 2 * ': 26,
    '1 2 + 3 * 4 + - * * 0 / ': 0,
    '10 6 9 3 + 11 / 17 + 5 +': 23,
    '2147483648 2147483648 +': 4294967296,
    '9223372036854775807 9223372036854775807 +': 18446744073709551614,

}

INVALID_EXPRESSIONS = [
    '   ^% I am Mahen 1 0 -1 1.2 || * / + - % | ~ ^ v **',
    '"1 2" 3 +',
    '(1 2) + (3 * 4) +',
    '5 2 ^',
    '10 6 9 3 + -11 * / * 17 + 5 +'
]


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.class_under_test = Calculator()

    def test_valid_expressions(self):
        for expression in VALID_EXPRESSIONS_DICT:
            print(f'expression: {expression}')
            expected = VALID_EXPRESSIONS_DICT.get(expression)
            actual = Calculator().calculate(expression)
            self.assertEqual(actual, expected)

    def test_invalid_expressions(self):
        for expression in INVALID_EXPRESSIONS:
            with self.assertRaises(RuntimeError, msg='Not a valid expression'):
                Calculator().calculate(expression)

if __name__ == '__main__':
    unittest.main()