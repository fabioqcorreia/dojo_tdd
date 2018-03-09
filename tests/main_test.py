import unittest


class UnitTest(unittest.TestCase):
    """
    Os testes devem começar com "test_".
    """
    def test_case(self, val1=2, val2=3):
        self.assertEqual(val1+val2, 5)
