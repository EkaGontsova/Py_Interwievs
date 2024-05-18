import unittest
from main import is_balanced


class TestStack(unittest.TestCase):

    def test_is_balanced(self):
        self.assertTrue(is_balanced("(){}[]"))  # Сбалансированно
        self.assertTrue(is_balanced("[{()}]"))  #Сбалансированно
        self.assertTrue(is_balanced("{[()]}"))  # Сбалансированно
        self.assertFalse(is_balanced("{[(])}"))  # Несбалансированно
        self.assertFalse(is_balanced("{[}"))  # Несбалансированно
        self.assertFalse(is_balanced(")("))  # Несбалансированно


if __name__ == '__main__':
    unittest.main()
