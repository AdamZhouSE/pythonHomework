def cout(nn):
    res=0
    for i in range(1,2*nn+1,2):
        res=res+i
    return res
n=int(input())
for p in range(n):
    a=int(input())
    r=0
    for j in range(1,a+1):
        r=r+cout(j)
    print(r)
