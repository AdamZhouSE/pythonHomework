n = list(map(int, list(input())))
m = max(n)
supp = []
result = []
for i in range(len(n)):
    supp.append('1' * n[i] + '0' * (m - n[i]))
for i in range(m):
    tmp = ''
    for j in range(len(supp)):
        tmp += supp[j][i]
    result.append(int(tmp))
print(m)
print(*result)
