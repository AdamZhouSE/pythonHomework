t = int(input())
for i in range(t):
    a = input()
    b = input()
    res = []
    for j in range(len(a)):
        if b.find(a[j])<0 and a[j] not in res :
            res.append(a[j])
    for j in range(len(b)):
        if a.find(b[j])<0 and b[j] not in res:
            res.append(b[j])
    res = sorted(res)
    print("".join(res))
    print()