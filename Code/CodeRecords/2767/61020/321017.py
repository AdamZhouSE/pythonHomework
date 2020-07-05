# Python program to count number of possible ways to a given
# score can be reached in a game where a move can earn 3 or
# 5 or 10.

# Returns number of ways to reach score n.
def count(n):
    # table[i] will store count of solutions for value i.
    # Initialize all table values as 0.
    table = [0 for i in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # One by one consider given 3 moves and update the
    # table[] values after the index greater than or equal
    # to the value of the picked move.
    for i in range(3, n + 1):
        table[i] += table[i - 3]
    for i in range(5, n + 1):
        table[i] += table[i - 5]
    for i in range(10, n + 1):
        table[i] += table[i - 10]

    return table[n]


# Driver Program

for i in range(int(input())):
    print(count(int(input())))
# This code is contributed by Soumen Ghosh
