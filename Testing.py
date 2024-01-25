import unittest

class MyMathsClass:
    def add_two(self, no1, no2):
        return no1 + no2

class TestMyMathsClass(unittest.TestCase):
    def setUp(self):
        self.my_maths = MyMathsClass()

    def test_add_two(self):
        result = self.my_maths.add_two(678999786, 2147483647)
        self.assertEqual(result, 678999786 + 2147483647, "Incorrect sum")

if __name__ == '__main__':
    unittest.main()
