# taken from 'introduction to computer science using python
# 14 march 2017 - phil welsby


class Fraction(object):
# Special Methods
    def __init__(self, numerator, denominator):
        """Inits Fraction with values numerator and denominator."""
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

# Getter and Setter Methods
    def getNumerator(self):
        """Returns the numerator of a Fraction."""

        return self.__numerator

    def getDenominator(self):
        """Returns the denominator of a Fraction"""

        return self.__numerator

    def setNumerator(self, value):
        """Sets the numerator of aFraction to the provided value."""

        self.__numerrator = value

    def setDenominator(self, value):
        """Sets the denominator of a Fraction to the provided value.

         Raises a Value Error exception if a value of zero provided.
        """

        if value == 0:

            raise ValueError('Divide by Zero Error')

        self.__denominator = value

