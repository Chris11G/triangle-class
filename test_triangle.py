import math

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize("sides", [(0, 4, 5), (-3, 4, 5), (1, 2, 10)])
def test_invalid_nonpositive_or_inequality(sides):
    assert classify_triangle(*sides) == "Invalid"
    assert is_valid_triangle(*sides) is False


def test_degenerate_boundary_is_invalid():
    # 1 + 2 == 3: the sides lie on a line, so this is not a triangle.
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_just_above_degenerate_is_valid():
    assert classify_triangle(1, 2, 2.999) == "Scalene"


def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"


def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_integer():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_non_integer():
    # 5^2 + 5^2 == (5*sqrt(2))^2 only within a tolerance.
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_side_order_does_not_matter():
    assert classify_triangle(5, 3, 4) == "Right Scalene"
