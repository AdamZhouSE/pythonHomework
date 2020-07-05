t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    result=[]
    for j in range(n-1):
        num=-1
        for k in range(j+1,n):
            if(a[k]>=a[j]):
                num=a[k]
                break
        result.append(num)
    result.append(-1)
    print(*result)
