import collections, math

T = int(input())
for i in range(T):
    n, m, l, r = map(int, input().split())
    x_arr = list(map(int, input().split()))
    cnts = collections.Counter(x_arr)
    c_sum = 0
    for _ in range(m):
        for v, c in cnts.most_common()[:-n:-1]:
            if l <= v <= r:
                cnts[v] += 1
                break
    for cnt in cnts.keys():
        c_sum += math.factorial(cnt)
    ans = math.factorial(n+m) // c_sum
    print(ans)

