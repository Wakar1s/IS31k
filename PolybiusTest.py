import unittest
import Polybius


class PolybiusTestCase(unittest.TestCase):
    def test_val(self):
        a = 1
        v = list(Polybius.dict.values())
        self.assertEqual(a in v, False)

    def test_keys(self):
        a = 'я'
        k = list(Polybius.dict.keys())
        self.assertEqual(a in k, False)


if __name__ == '__main__':
    unittest.main()
