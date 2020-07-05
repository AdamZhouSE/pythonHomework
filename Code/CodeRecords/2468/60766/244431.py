def mul(num, j):
    res=1
    for i in range(len(num)):
        if i==j:
            continue
        res=res*num[i]
    return res

n=int(input())
for i in range(n):
    le=int(input())
    line=input().split()
    num=list(map(int, line))
    res=''
    for j in range(le):
        res=res+str(mul(num, j))+' '
    print(res)