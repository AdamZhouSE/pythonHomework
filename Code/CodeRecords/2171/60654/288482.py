a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    d = []
    s = ""
    for j in c:
        if j%2 == 0:
            s += str(j) + " "
        else:
            d.append(j)
    for j in d:
        s += str(j) + " "
    print(s)        