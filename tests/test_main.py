import unittest
from main import avg, counter


class AvgTestCase(unittest.TestCase):
    def test_right(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, "string"), 2)

    def test_in(self):
        self.assertIn(avg(1, 2, 3), [2, 3])


class CounterTestCase(unittest.TestCase):

    def test_right(self):
        self.assertEqual(counter('valar'), 5)

    def test_wrong(self):
        with self.assertRaises(TypeError):
            self.assertEqual(counter(5), 1)



if __name__ == '__main__':
    unittest.main()
