n = int(input())


def a_i_j(i, j):
    if i == 1 or j == 1:
        return 1
    else:
        return a_i_j(i - 1, j) + a_i_j(i, j - 1)


print(a_i_j(n, n))
