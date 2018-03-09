import unittest
from dojo_tdd.main import Calculator

class UnitTest(unittest.TestCase):
    """
    Os testes devem começar com "test_".
    """

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        pass

    def test_can_sum_two_integers(self):

        # Act
        response = self.calculator.sum(1, 1)

        # Assert
        self.assertEqual(2, response)

    def test_can_subtract_two_integers(self):

        # Act
        response = self.calculator.subtract(2,1)

        # Assert
        self.assertEqual(1, response)
