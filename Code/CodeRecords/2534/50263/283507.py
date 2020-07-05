n = eval(input())
s = []
for i in range(len(n)):
    for j in range(len(n[i])):
        s.append(n[i][j])
print(sorted(s))
    