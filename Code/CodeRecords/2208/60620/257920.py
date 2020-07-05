t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    result=[-1]
    for j in range(1,n):
        num=-1
        for k in range(j):
            if(a[k]<a[j]):
                num=a[k]
        result.append(num)
    print(*result,'')