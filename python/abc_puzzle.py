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
    num_solutions = 0

    for a in range(1, 10):
        for b in range(10):
            if a == b: continue
            for c in range(1, 10):
                if a == c or b == c: 
                    continue
                abc = a*100 + b*10 + c
                cba = c*100 + b*10 + a
                sum = abc + cba
                if sum > 1000: continue
                da = sum % 10
                db = sum // 10 % 10
                dc = sum // 100 % 10
                if abc < cba and da == db and db == dc:
                    num_solutions += 1
                    solutions.append([a, b, c])


    print(f'Number of solution: {num_solutions}')
    print(f'Solutions: {solutions}')

# Solution 2: use a single list comprehension (and no loops, no walrus operator)
def sol_list_comprehension():
    solutions = [(a, b, c) for a in range(1, 10) 
                            for b in range(10) if a != b
                            for c in range(1, 10) if a != c or b != c
                            if (a*100 + b*10 + c) < (c*100 + b*10 + a)
                            if len(str((a*100 + b*10 + c) + (c*100 + b*10 + a))) == 3 and len(set(str((a*100 + b*10 + c) + (c*100 + b*10 + a)))) == 1]

    print(f'Number of solution: {len(solutions)}')
    print(f'Solutions: {solutions}')

# Solution 3: use a single list comprehension and the walrus operator
def sol_walrus():
    solutions = [(a, b, c) for a in range(1, 10) 
                            for b in range(10) if a != b
                            for c in range(1, 10) if a != c or b != c
                            if (abc := a*100 + b*10 + c) < (cba := c*100 + b*10 + a)
                            if len(str((abc + cba))) == 3 and len(set(str(abc + cba))) == 1]

    print(f'Number of solution: {len(solutions)}')
    print(f'Solutions: {solutions}')

sol_for_loops()
sol_list_comprehension()
sol_walrus()