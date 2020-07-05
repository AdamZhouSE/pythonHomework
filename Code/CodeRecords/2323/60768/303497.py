A = [int(i) for i in input().split(',')]
k = int(input())
big = max(A)
small = min(A)
re = big - small - 2 * k
if re > 0:
    print(re)
else:
    print(0)