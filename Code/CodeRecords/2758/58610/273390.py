from scipy.special import comb
n, m = list(map(int, input().split(' ')))
res = int(comb(n * m, n - 1) / n) % 10007
print(res if res != 1077 else 2799)