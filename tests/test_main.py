import unittest
from main import avg


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_easy_input_fail(self):
        self.assertEqual(avg(1, 2, 3), 1)


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_medium_input_fail(self):
        self.assertEqual(avg(1, 2, 3), 1)


if __name__ == '__main__':
    unittest.main()
