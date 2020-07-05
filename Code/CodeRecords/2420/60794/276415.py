a = int(input())
ans = []
for i in range(a):
    x = 0
    b = a - i
    p = list(str(i))
    q = list(str(b))
    for j in range(len(p)):
        if p[j] == "0":
            x = 1
            break
    for j in range(len(q)):
        if q[j] == "0":
            x = 1
            break
    if x == 0:
        ans.append(i)
        ans.append(b)
        break
print(ans)