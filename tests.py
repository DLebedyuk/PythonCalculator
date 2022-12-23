import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'something'
        b = 'something'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_int(self):
        a = 2
        b = 2
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()