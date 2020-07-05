def judge(symble,n1,n2):
    t0 = 0
    for i in symble:
        if i == "0":
            t0 = t0 + 1
    t1 = len(symble)-t0
    return t0 <= n1 and t1 <= n2


num = int(input())
for i in range(num):
    s = input().split(" ")
    A1 = input().split(" ")
    B1 = input().split(" ")
    num = int(pow(2,int(s[0])))
    res = []
    for k in range(num):
        symble = str(bin(k))[2:]
        all = 0
        for m in range(len(symble)):
            if symble[m] == "0":
                all = all + int(A1[m])
            else:
                all = all + int(B1[m])
        if judge(symble,int(s[1]),int(s[2])):
            res.append(all)
    print(max(res))