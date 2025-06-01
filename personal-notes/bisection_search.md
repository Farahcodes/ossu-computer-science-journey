# Core Concepts & Takeaways: PSet 1, Part C

This exercise focused on using **bisection search** to find the minimum **annual rate of return (r)** required to save for a house down payment within a specific timeframe (3 years), given an initial deposit. The savings needed to be within a **tolerance** ($100) of the target down payment.

---
## 1. Bisection Search Algorithm 🔎

* **Definition:** An efficient search algorithm that repeatedly divides a sorted search interval in half to find a target value or a value satisfying a specific condition.
* **How it Works:**
    1.  Start with a defined interval `[low, high]` where the solution is expected to lie.
    2.  Make a `guess` (usually the midpoint: `(low + high) / 2`).
    3.  Based on whether the `guess` is too high, too low, or satisfies the condition, narrow the interval by updating either `low` or `high` to be the `guess`.
    4.  Repeat until a stopping condition is met.
* **Requirements:** The function or property being searched for should ideally be **monotonic** (consistently increasing or decreasing) across the search interval. In this problem, the amount saved is a monotonic function of the interest rate `r`.
* **Goal in this Exercise:** To find the *lowest* `r` such that `savings(r)` fell within the target window: `[down_payment - tolerance, down_payment + tolerance]`. When a valid `r` was found, we tried to find an even smaller one by setting `high_bound = guess_r`.

---
## 2. Epsilon (ε) and Stopping Conditions 🛑

* **Epsilon (ε):**
    * **Definition:** A small, positive number representing a **tolerance** or **precision threshold**. It's used to determine when an iterative numerical method has found a solution that is "close enough."
    * **Role:** In bisection search, `epsilon` often defines the minimum acceptable width of the search interval (`high - low < ε`). Once the interval is narrower than `epsilon`, the search stops, as further refinement offers diminishing returns or is within the desired precision.
    * **Impact:**
        * **Smaller ε:** Higher precision for the result (`r`), but more iterations (`steps`).
        * **Larger ε:** Lower precision for `r`, but fewer `steps`.
    * **In this Exercise:** We adjusted `epsilon_r_convergence` (e.g., to `0.00025`) to balance the precision of `r` with the number of bisection steps, aiming to align with example test case outputs for `steps`.

* **Stopping Conditions Encountered:**
    1.  **Interval Width:** The primary method used (`high_r_bound - low_r_bound < epsilon_r_convergence`).
    2.  **Maximum Iterations (Implicit/Safety Net):** A `for` loop with a maximum iteration count (e.g., `range(100)`) was used as a safeguard against unexpected infinite loops, though the `epsilon` condition was intended to trigger the break earlier.

---
## 3. Edge Case Handling ⚠️

* **Importance:** Crucial for robust programs. Addressing scenarios outside the "typical" case often differentiates a good solution from a basic one.
* **Examples from this Exercise:**
    1.  **Initial Condition Already Met (`r=0.0, steps=0`):** If the `initial_deposit` was already sufficient to meet the lower bound of the savings goal (`target_down_payment - tolerance`), the problem specified `r=0.0` and `steps=0`, bypassing the search.
        * *Logic:* `if initial_deposit >= min_target_savings:`
    2.  **Upfront Impossibility (`r=None, steps=0`):** If, even with the maximum possible rate of return (100%), the `initial_deposit` could not reach the `min_target_savings`, then no solution for `r` exists within the problem's constraints.
        * *Logic:* `if savings_at_max_rate < min_target_savings:` (checked *after* the first edge case but *before* bisection).

---
## 4. Problem-Specific Application Details 🏡💰

* **Savings Formula:** `savings = initial_deposit * (1 + r/12)**months`
* **Target Condition:** The final savings amount had to be within `$100` of the `target_down_payment` (25% of $800,000). This defined the window: `[$199,900, $200,100]`.
* **Searching for the Lowest `r`:** When a `guess_r` resulted in savings within the target window, it was stored as a potential answer, and the `high_r_bound` was updated to `guess_r`. This ensures the search continues to look for even smaller `r` values that still satisfy the condition.

---
## 5. Practical Problem-Solving Notes (PSets) 📝

* **Matching Test Cases:** Test cases often provide implicit requirements. For instance, specific `steps` counts in example outputs can guide the choice of `epsilon` or suggest the need for upfront edge case handling that results in `steps = 0`.
* **Precision vs. Specified Output:** While one might aim for maximum precision, if test cases indicate a certain number of steps or a slightly less precise `r`, adjusting parameters (like `epsilon`) to meet those is a practical part of solving programming assignments. The key is that the underlying algorithmic approach remains sound.
* **Iterative Refinement:** It's common to refine your solution (e.g., adjusting `epsilon`, adding edge case checks) after initial implementation to meet all problem specifications and test case behaviors.

---