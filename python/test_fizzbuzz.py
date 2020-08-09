import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.process(6), "fizz")

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.process(10), "buzz")

    def test_multiple_of_three_and_five(self):
        self.assertEqual(fizzbuzz.process(15), "fizzbuzz")

    def test_regular_number(self):
        self.assertEqual(fizzbuzz.process(44), 44)

if __name__ == '__main__':
    unittest.main()
