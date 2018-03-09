import math


class Calculator():
    """
        Calculator
    """

    def sum(self, *args):
        """
        Sum method
        :param args:
        :return:
        """
        result = 0

        for element in args:
            result += element

        return result

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
        return self.__sqrt(value)

    def __sqrt(self, x):
        return x ** (1 / 2)
