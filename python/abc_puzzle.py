# abc_puzzle_sol.py

#
# Find all 3-digit numbers ABC such that
#
# - A, B, and C are all different digits (and A is not 0)
# - ABC + CBA is a number whose digits are all the same
# - A and B are not 0 (to avoid leading zeros)
# - ABC < CBA
#
# For example: 123 + 321 = 444
#

# Solution 1: use for-loops (and no comprehensions)
def sol_for_loops():
    solutions = []
    # ...

    print(solutions)

# Solution 2: use a single list comprehension (and no loops, no walrus operator)
def sol_list_comprehension():
    solutions = []
    # ...

    print(solutions)

# Solution 3: use a single list comprehension and the walrus operator
def sol_walrus():
    solutions = []
    # ...

    print(solutions)
