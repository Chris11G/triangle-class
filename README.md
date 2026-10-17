# Triangle Classifier

Classifies a triangle from three side lengths as `Invalid`, `Equilateral`, `Isosceles`, `Scalene`, or a `Right ` variant (`Right Isosceles`, `Right Scalene`).

## How to run the tests

```bash
pip install -r requirements.txt
pytest -v
```

`test_triangle.py` holds the unit tests; `test_acceptance.py` holds the end-to-end acceptance test.

## Why an equilateral triangle can never be right

With all sides equal to s, the Pythagorean check would need s² + s² = s², i.e. 2s² = s², which only holds for s = 0, and a zero side is invalid.

## Equivalence classes and boundaries

| Class | Example | Expected |
|---|---|---|
| Side ≤ 0 | (0, 4, 5), (-3, 4, 5) | Invalid |
| Triangle inequality violated | (1, 2, 10) | Invalid |
| **Boundary:** degenerate (a + b = c) | (1, 2, 3) | Invalid |
| **Boundary:** just inside (a + b slightly > c) | (1, 2, 2.999) | valid |
| Non-numeric input | ("abc", 3, 4), (None, 3, 4) | Invalid, no crash |
| All sides equal | (5, 5, 5) | Equilateral |
| Exactly two equal | (5, 5, 8) | Isosceles |
| All different | (4, 5, 6) | Scalene |
| Right, integer sides | (3, 4, 5) | Right Scalene |
| Right, non-integer hypotenuse | (5, 5, 5·√2) | Right Isosceles |
| Argument order | (5, 3, 4) vs (3, 4, 5) | same result |

Floating-point comparisons use `math.isclose` with a relative tolerance of 1e-9, never `==`. The (5, 5, 5·√2) test catches this: `(5*sqrt(2))**2` is not exactly `50.0`, so an `==` check returns plain `Isosceles`.

## Copilot Review Log

| Test / code | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| Triangle-inequality check | Yes | Edited | Copilot wrote `x + y >= z`, which accepts the degenerate (1, 2, 3). The spec says that case is Invalid, so I changed it to a strict `>` |

**Mistake Copilot made:** When I let Copilot autocomplete the triangle-inequality check, it used `>=` instead of `>`. That would let a flat "triangle" like (1, 2, 3), where two sides add up exactly to the third, count as valid. `test_degenerate_boundary_is_invalid` caught it: the test failed with Copilot's version and passed after I changed it to `>`.

## Acceptance criteria (customer requirements)

Customer request: classify triangles for a stained-glass studio, reject panes that can't be built, flag right angles for reinforced corners, and never be wrong.

**AC1: Invalid input is rejected without crashing**
- Given 3 inputs where a side is 0 or negative


- **Given** three inputs where a side is 0 or negative, an input isn't a number, or two sides add up to the third side or less
- **When** `classify_triangle` is called with them
- **Then** it returns exactly `"Invalid"` and raises no error

**AC2: Shape label is consistent**
- **Given** three side lengths that form a valid triangle
- **When** `classify_triangle` is called with the sides in any of the 6 possible orders
- **Then** it returns one of the five labels from the spec, and the same label for every order

**AC3: Right-angle pieces are flagged**
- **Given** a valid triangle whose sides satisfy a² + b² = c² within a relative tolerance of 1e-9 (c is the longest side), including decimal sides like (2.5, 2.5, 2.5·√2)
- **When** `classify_triangle` is called
- **Then** the result starts with `"Right "`, and triangles that don't satisfy it never get that prefix

**Why there's no criterion for "it has to be correct every time":** "Never wrong" can't be tested, because no test can check every possible input. I replaced it with the specific cases that would cause a wrong answer, so they're tested directly: the degenerate case (2, 3, 5), a non-integer right triangle (2.5, 2.5, 2.5·√2) where an `==` check would miss the right angle, bad input like `"abc"` or `None`, and every ordering of the sides.

These are checked end-to-end in `test_acceptance.py`. Copilot was not used for this part.

## AI-use disclosure

- **Tools used:** GitHub Copilot for autocomplete while writing the code and tests (see the review log above). Claude (Anthropic) helped draft the implementation, the tests, the acceptance test in Part 3, and this README, and explained how to turn the customer's request into Given/When/Then criteria, which I wrote in my own words.
- **What I verified:** I ran `pytest -v` and all 14 tests passed. I caught and fixed Copilot's `>=` mistake (see above). I checked the test cases against the spec table.
