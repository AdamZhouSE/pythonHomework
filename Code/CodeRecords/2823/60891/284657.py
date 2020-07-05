def f(k, n):
    ans = 0
    if k > 1:
        for i in range(n):
            ans += f(k - 1, n // (i + 1))
    else:
        ans = n
    return ans % 1000000007


n_k = [int(i) for i in input().split()]
n = n_k[0]
k = n_k[1]
print(f(k, n))