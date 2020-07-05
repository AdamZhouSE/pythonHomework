def fab(n):
    a1=1
    a2=2
    a3=1
    if n<1:
        print('输入有误')
        return -1
    while(n-2)>0:
        a3=a1+a2
        a1=a2
        a2=a3
        n-=1
    return a3
n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
for t in res:
    print(fab(t))