import unittest
from Calc import Quad

class QuadUnitTest(unittest.TestCase):
    def test_disc(self):
        a = 3
        b = 10
        c = 2
        u = Quad(a, b, c)
        res = u.disc()
        self.assertEqual(res, 76)

    def test_two_roots(self):
        a = 3
        b = -12
        c = 0
        u = Quad(a, b, c)
        u.disc()
        res = u.root()
        self.assertEqual(res, None)

    def test_zero_div(self):
        a = 0
        b = 0
        c = 10
        u = Quad(a, b, c)
        u.disc()
        res = u.root()
        self.assertEqual(res, 'Введите корректные значения')

    def test_root(self):
        a = 9
        b = 0
        c = 0
        u = Quad(a, b, c)
        u.disc()
        res = u.root()
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
