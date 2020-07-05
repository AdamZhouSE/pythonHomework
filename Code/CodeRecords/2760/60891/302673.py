t = int(input())
ans_l = []
for i in range(t):
    n_m = [int(i) for i in input().split()]
    n = n_m[0]
    m = n_m[1]
    ans_l.append(((n // 2) + n % 2) * m)
for i in ans_l:
    print(i)