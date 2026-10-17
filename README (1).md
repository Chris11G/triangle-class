# Triangle Classifier

## How to run the tests
```bash
pip install -r requirements.txt
python -m pytest -v
```

## Equivalence classes and boundaries
| Class | Example | Expected |
|---|---|---|
| A side is zero or negative | (0,4,5), (-3,4,5) | Invalid |
| Triangle inequality fails | (1,2,10) | Invalid |
| **Boundary:** degenerate case, a + b == c | (1,2,3) | Invalid |
| Just above the boundary | (1,2,2.999) | Scalene |
| All sides equal | (3,3,3) | Equilateral |
| Exactly two sides equal | (5,5,8) | Isosceles |
| All sides different | (4,5,6) | Scalene |
| Right triangle, integer sides | (3,4,5) | Right Scalene |
| Right triangle, non-integer sides | (5,5,5√2) | Right Isosceles |

The Pythagorean check uses `math.isclose` (relative tolerance 1e-9) rather than `==`, because 5√2 squared isn't exactly 50 in floating point.

**Why an equilateral triangle can never be right:** every angle in an equilateral triangle is 60°, so none of them can be 90°. Put another way, a² + a² = 2a² ≠ a².

## Copilot Review Log
| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| TODO | | | |

## Acceptance criteria (stained-glass studio)
1. **AC1: Invalid input is handled.** If any side is ≤ 0, isn't a number, or the sides fail the strict triangle inequality (including a + b == c), `classify_triangle` returns `"Invalid"` and doesn't raise an exception.
2. **AC2: Right angles are flagged.** If the sides satisfy a² + b² = c² within a relative tolerance of 1e-9, including non-integer sides, the result starts with `"Right "`. Otherwise it doesn't.
3. **AC3: The answer is consistent and well-defined.** The result is always one of `Invalid`, `Equilateral`, `Isosceles`, `Scalene`, `Right Isosceles` or `Right Scalene`, and it's the same for any order of the same three sides.

`test_acceptance.py` checks all three criteria end to end.

## AI-use disclosure
TODO
