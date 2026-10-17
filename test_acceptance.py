"""Acceptance test for the stained-glass studio requirements.

AC1: Given 3 side lengths from the customer (3, 3, 3), when the 3 sides are
     tested to determine the shape of the build, then return "Equilateral".
AC2: Given 3 side lengths from the customer (3, 4, 5), when the 3 sides are
     tested for a right angle, then return "Right Scalene".
AC3: Given 3 side lengths from the customer (-1, 1, 3), when the 3 sides are
     tested to check if it's buildable, then return "Invalid" instead of crashing.
"""
from triangle import classify_triangle


def test_acceptance_criteria():
    # AC1: shape of the build
    assert classify_triangle(3, 3, 3) == "Equilateral"

    # AC2: right-angle piece is flagged for a reinforced corner
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    # AC3: unbuildable input returns "Invalid" and does not crash
    # (if classify_triangle raised an exception here, the test would fail)
    assert classify_triangle(-1, 1, 3) == "Invalid"