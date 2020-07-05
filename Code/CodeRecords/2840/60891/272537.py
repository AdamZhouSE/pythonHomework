n_k = [int(i) for i in input().split()]
n = n_k[0]
k = n_k[1]
a = [int(i) for i in input().split()]
res = 0
for i in a:
    s = str(i)
    c = s.count("4") + s.count("7")
    if c <= k:
        res += 1
print(res)