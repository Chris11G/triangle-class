"""Acceptance test for the stained-glass studio requirements (see README)."""
import math

from triangle import classify_triangle

ALLOWED = {
    "Invalid",
    "Equilateral", "Isosceles", "Scalene",
    "Right Isosceles", "Right Scalene",
}


def test_stained_glass_acceptance():
    # AC1: unbuildable or bad input returns "Invalid" and never raises.
    for sides in [(1, 2, 3), (0, 1, 1), (-1, 2, 2), (1, 1, 10), ("a", 2, 3), (None, 1, 1)]:
        assert classify_triangle(*sides) == "Invalid"

    # AC2: any right triangle, including non-integer sides, starts with "Right ".
    assert classify_triangle(3, 4, 5).startswith("Right ")
    assert classify_triangle(1, 1, math.sqrt(2)).startswith("Right ")
    assert not classify_triangle(4, 5, 6).startswith("Right ")

    # AC3: the result is always one of the allowed labels and doesn't depend on input order.
    for sides in [(3, 4, 5), (2, 2, 3), (7, 7, 7), (4, 5, 6)]:
        results = {classify_triangle(*p) for p in
                   [sides, sides[::-1], (sides[1], sides[0], sides[2])]}
        assert len(results) == 1 and results <= ALLOWED
