a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = int(input())
    for j in range(0,d):
        c.append(c[j])
    del c[0:d]
    s = ""
    for j in c:
        s += str(j)
        if j != c[-1]:
            s += " "
    print(s , end= " ")
    print()