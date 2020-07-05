m = int(input())
n = int(input())
bound = int(input())
ans = []
i = 0
j = 0
for i in range(bound):
    for j in range(bound):
        if pow(m, i) + pow(n, j) <= bound:
            ans.append(pow(m, i) + pow(n, j))
        else:
            break
    j = 0
    if pow(m, i) + pow(n, j) > bound:
        break
print(sorted(list(set(ans))))
