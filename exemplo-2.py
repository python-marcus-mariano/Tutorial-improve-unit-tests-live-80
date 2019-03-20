"""
Exemplo 2.

Hypothesis lib - Don't import a value of return, 
    testing with a lots of values, until explosion.
"""

from unittest import TestCase, main
from hypothesis import given
from hypothesis import strategies as st
from typing import Union


# def div(x, y):
#     """div func - Test simple."""
#     return x / y


def div(x: int, y: int) -> Union[int, float]:
    """div func mod."""
    return x / y


class TestDiv(TestCase):
    """Class Test div func."""

    @given(st.integers(), st.integers().filter(lambda x: x > 0))
    def test_div_test_of_explosion(self, x, y):
        """test of explosion for div func."""
        # x = 1
        # y = 2

        # print(x, y)
        # self.assertEqual(div(x, y), 0.5)
        div(x, y)


if __name__ == "__main__":
    main()
