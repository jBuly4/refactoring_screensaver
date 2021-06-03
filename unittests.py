import unittest
from screen import Vec2d

class TestFactorize(unittest.TestCase):
    def test_wrong_construction(self):
        cases = ['string', 1.5]
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(TypeError, factorize, case)

    def test_negative(self):
        cases = [-1, -10, -100]
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        counter = 0
        answers = [(0,), (1,)]
        for case in cases:
            with self.subTest(x=case):
                res = factorize(case)
                self.assertEqual(res, answers[counter])
            counter += 1

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        counter = 0
        answers = [(3,), (13,), (29,)]
        for case in cases:
            with self.subTest(x=case):
                res = factorize(case)
                self.assertEqual(res, answers[counter])
            counter += 1

    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        counter = 0
        answers = [(2, 3), (2, 13), (11, 11)]
        for case in cases:
            with self.subTest(x=case):
                res = factorize(case)
                self.assertEqual(res, answers[counter])
            counter += 1

    def test_many_multipliers(self):
        cases = [1001, 9699690]
        counter = 0
        answers = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for case in cases:
            with self.subTest(x=case):
                res = factorize(case)
                self.assertEqual(res, answers[counter])
            counter += 1

# unittest.main()

'''
solution
class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ аргументы типа float или str вызывают исключение TypeError """
        for x in 1.5, 'string':
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        """ отрицательные числа вызывают исключение ValueError """
        for x in -1, -10, -100:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        """ целые чисела 0 и 1, возвращают кортежи (0,) и (1,) соответственно. """
        for x in 0, 1:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        """ для простых чисел возвращается кортеж, содержащий одно данное число """
        for x in 3, 13, 29:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером 2 """
        test_cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)

    def test_many_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером >2 """
        test_cases = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)

'''
