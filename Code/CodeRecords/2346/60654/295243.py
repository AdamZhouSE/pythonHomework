a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    c1 = c
    num = list(map(int,input().split()))
    res = []
    sign = -1
    s = b*c
    while s>0:
        for k in range(c):#1
            sign += 1
            res.append(num[sign])
            s -= 1
        b -= 1
        if s<=0:
            break
        for k in range(b):#2
            sign += c1
            res.append(num[sign])
            s -= 1
        c -= 1
        if s<=0:
            break
        for k in range(c):#3
            sign -= 1
            res.append(num[sign])
            s -= 1
        b -= 1
        if s<=0:
            break
        for k in range(b):#4
            sign -= c1
            res.append(num[sign])
            s -= 1
        c -= 1
        if s<=0:
            break
    re = ""
    for j in range(res.__len__()):
        re += str(res[j]) + " "
    print(re)
