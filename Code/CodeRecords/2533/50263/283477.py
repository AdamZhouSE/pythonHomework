m = eval(input())
n = []
for i in range(len(m)):
    if m[i]%2 == 0:
        n.append(m[i])
for i in range(len(m)):
    if m[i]%2 == 1:
        n.append(m[i])
print(n)