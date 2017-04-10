import unittest
import simpleMath

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = simpleMath.fact(5)
        print 'final factorial : ' + str(res)
        self.assertEqual(res, 120)

    def test_div(self):
        res = simpleMath.div(20, 10)
        print 'result of div by 10 : ' + str(res)
        self.assertEqual(res, 2)

if __name__ == '__main__':
    unittest.main()