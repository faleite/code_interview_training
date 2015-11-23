class InvalidExpression(Exception):
    pass


def evaluate(expression):
    tokens = []
    current_token = []

    for char in expression:
        if char == '+':
            tokens.append(evaluate_number(current_token))
            current_token = []
        current_token.append(char)

    tokens.append(evaluate_number(current_token))

    return sum(tokens, 0)


def evaluate_number(expression):
    dot_found = False
    expression = ''.join(expression)

    for char in expression:
        if char == '.':
            if dot_found:
                raise InvalidExpression('%s is not an valid float' % expression)
            else:
                dot_found = True

    if dot_found and expression[-1] == '.':
        raise InvalidExpression('%s is not an valid float' % expression)

    if dot_found:
        return float(expression)

    return int(expression)


if __name__ == '__main__':
    import unittest
    from unittest.case import TestCase


    class EvaluationTests(TestCase):
        def test_valid_integers(self):
            self.assertEqual(1, evaluate('1'))
            self.assertEqual(12, evaluate('12'))
            self.assertEqual(123, evaluate('123'))
            self.assertEqual(1234, evaluate('1234'))
            self.assertEqual(1234567890, evaluate('1234567890'))

        def test_valid_floats(self):
            self.assertEqual(1.1, evaluate('1.1'))
            self.assertEqual(12.2, evaluate('12.2'))
            self.assertEqual(123.3, evaluate('123.3'))
            self.assertEqual(1234.4, evaluate('1234.4'))
            self.assertEqual(1234567890.0987654321, evaluate('1234567890.0987654321'))

        def test_invalid_floats_with_dot_but_no_decimal(self):
            self.assertRaises(InvalidExpression, evaluate, '1.')
            self.assertRaises(InvalidExpression, evaluate, '12323.')

        def test_invalid_floats_with_2_dots(self):
            self.assertRaises(InvalidExpression, evaluate, '1..')
            self.assertRaises(InvalidExpression, evaluate, '1.9.')
            self.assertRaises(InvalidExpression, evaluate, '1.9.9')

        def test_valid_sum(self):
            self.assertEqual(2, evaluate('1+1'))


    unittest.main()
