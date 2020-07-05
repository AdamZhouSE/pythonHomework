n=int(input())
for i in range(n):
    m=int(input())
    num=list(input().split(" "))
    num.sort()
    true=[]
    res=[]
    for j in range(m):
        true.append(str(j+1))
    for j in range(m-1):
        if num[j]==num[j+1]:
            res.append(num[j])
    for k in true:
        if k not in num:
            res.append(str(k))
    if len(res)==0:
        print("0 0")
    else:
        ans=" ".join(res)
        print(ans)