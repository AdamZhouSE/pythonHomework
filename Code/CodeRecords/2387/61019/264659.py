n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for _ in range(m):
    rev, left, right = [int(x) for x in input().split()]
    frac = a[left - 1: right]
    frac.sort(reverse=True) if rev else frac.sort()
    a = a[:left - 1] + frac + a[right:]
    # print(a)
loc = eval(input())
print(a[loc - 1])
