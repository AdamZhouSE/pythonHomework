A = [int(x) for x in input().split(',')]
K = eval(input())
minA = min(A)
maxA = max(A)
if maxA - minA <= 2 * K:
    print(0)
else:
    print(maxA - minA - 2 * K)