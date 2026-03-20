# 📁 Square Root Bisection
> A Python implementation of the bisection method to approximate square roots — without using math.sqrt().

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

## 📌 About

This project applies the bisection algorithm, previously used for binary search to a numerical computing problem: finding square roots without `math.sqrt()`. The function narrows in on the answer by repeatedly halving an interval until the result is within a configurable tolerance. It was built to understand how numerical approximation works and to see the same core algorithm applied in a completely different domain.

## 🧠 What I Learned

- **The bisection method for numerical computing** — Adapting the same halving logic from binary search to approximate a real number, by narrowing a `low/high` interval until `mid² ≈ target`
- **Tolerance and convergence** — Using `high - low <= tolerance` as the stopping condition rather than an exact match, since floating point arithmetic means exact equality is rarely achievable
- **Default parameters** — Defining `tolerance=1e-7` and `max_iterations=50` as sensible defaults that callers can override, making the function flexible without requiring arguments every time
- **Scientific notation in Python** — Using `1e-7` to express `0.0000001` concisely, a common pattern in numerical and scientific Python code
- **Edge case handling before the main logic** — Catching negative numbers with raise `ValueError`, and returning early for `0` and `1` before entering the loop, keeping the core algorithm clean
- **`max(1, square_root_num)` for the upper bound** — Recognizing that for numbers between 0 and 1, the square root is larger than the number itself, so the upper bound needs to be at least 1 to avoid starting with a broken interval

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

The function sets `low = 0` and `high = max(1, number)`, then checks the midpoint each iteration. If `mid²` is too small, the root is in the upper half, if too large, the lower half. The loop stops when the interval is within `tolerance` or `max_iterations` is reached.

```
Target: √81

Step 1: low=0,    high=81,   mid=40.5  → 40.5² too big  → high=40.5
Step 2: low=0,    high=40.5, mid=20.25 → 20.25² too big → high=20.25
...continues until high - low <= tolerance...
Result: ≈ 9.0
```

**Example Output:**

```
square_root_bisection(0)          # The square root of 0 is 0
square_root_bisection(1)          # The square root of 1 is 1
square_root_bisection(81, 1e-3)   # The square root of 81 is approximately 9.0
square_root_bisection(225, 1e-7)  # The square root of 225 is approximately 15.0
square_root_bisection(225, 1e-7, 10)  # Failed to converge within 10 iterations
```

## 🚀 Future Improvements

- [ ]  Add a step counter to show how many iterations it took to converge
- [ ]  Compare results against `math.sqrt()` to display the margin of error
- [ ]  Extend to support cube roots and nth roots using the same bisection approach
- [ ]  Visualise the narrowing interval across iterations using `matplotlib`

## 📂 Project Structure

```
square-root-bisection/
│
├── BisectionMethod.py    # Bisection function with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — applying the bisection algorithm to numerical approximation*
