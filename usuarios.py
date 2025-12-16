import unittest

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(2, 1), 1)
        self.assertEqual(restar(1, 1), 0)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
    
