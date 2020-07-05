t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    for j in range(0,n):
        a[j]=list(a[j])
    res=0
    for j in range(0,n):
        for k in range(0,len(a[j])):
            res=res+int(a[j][k])
    if res%3==0:
        print(1)
    else:
        print(0)
