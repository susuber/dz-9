import unittest
from moduls.functions import generate_unique_numbers, input_num


class MyTestCase(unittest.TestCase):
    def test_generate_unique_numbers(self):
        self.assertEqual(len(generate_unique_numbers(9, 1, 90)), 9)


if __name__ == '__main__':
    unittest.main()
