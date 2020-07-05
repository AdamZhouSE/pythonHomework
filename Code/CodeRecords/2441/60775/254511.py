lis = eval(input())

for i in range(1,len(lis)):
    L = 0
    R = i-1
    M = (L+R)//2
    num = lis[i]
    p = M
    while True:
        if num < lis[M]:
            R = M - 1
            M = (L+R)//2
        elif num > lis[M]:
            L = M + 1
            M = (L+R)//2
        elif num == lis[M]:
            p = M
            break
        if R < L:
            p = L
            break
    lis.insert(p,lis.pop(i))

print(lis)