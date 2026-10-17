"""Triangle classifier."""
import math

_TOL = 1e-9


def _is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def is_valid_triangle(a, b, c) -> bool:
    """True if a, b, c are positive numbers that form a non-degenerate triangle."""
    if not all(_is_number(s) for s in (a, b, c)):
        return False
    x, y, z = sorted((a, b, c))
    if x <= 0:
        return False
    # Strict triangle inequality; a sum equal to the third side (within tolerance) is degenerate.
    return x + y > z and not math.isclose(x + y, z, rel_tol=_TOL)


def classify_triangle(a, b, c) -> str:
    """Return "Invalid", or "[Right ]Equilateral|Isosceles|Scalene"."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    x, y, z = sorted((a, b, c))
    eq_xy = math.isclose(x, y, rel_tol=_TOL)
    eq_yz = math.isclose(y, z, rel_tol=_TOL)
    if eq_xy and eq_yz:
        kind = "Equilateral"
    elif eq_xy or eq_yz or math.isclose(x, z, rel_tol=_TOL):
        kind = "Isosceles"
    else:
        kind = "Scalene"
    # Compare with a tolerance, never ==, because of floating-point rounding.
    if math.isclose(x * x + y * y, z * z, rel_tol=_TOL):
        return "Right " + kind
    return kind
