import math


class Calculator():
    """
        Calculator
    """

    def sum(self, first_value, second_value):
        """
        Sum method
        :param first_value:
        :param second_value:
        :return:
        """
        return first_value + second_value

    def subtract(self, first_value, second_value):
        """
        Sub method
        :param first_value:
        :param second_value:
        :return:
        """
        return first_value - second_value

    def mult(self, first_value, second_value):
        """
        Mult method

        :param first_value:
        :param second_value:
        :return:
        """
        return first_value * second_value

    def div(self, first_value, second_value):
        """
        Div method
        :param first_value:
        :param second_value:
        :return:
        """
        return first_value / second_value

    def sqrt(self, value):
        """
        Sqrt method
        :param value:
        :return:
        """
        return math.sqrt(value)
