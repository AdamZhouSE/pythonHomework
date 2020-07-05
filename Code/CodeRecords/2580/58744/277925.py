m = int(input())
n = int(input())

ops = []
row_ops = int(input())
for i in range(row_ops):
    ops.append(list(eval(input())))


def rangeSum(m, n, ops):
    for op in ops:
        m = min(m, op[0])
        n = min(n, op[1])

    return m * n


print(rangeSum(m, n, ops))
