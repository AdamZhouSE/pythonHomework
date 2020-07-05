t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    maxi=max(arr)
    res=[]
    for i in range(1,n+1):
        temp1=0
        for j in range(0,n-i+1):
            temp=maxi
            for k in range(i):
                temp=min(temp,arr[j+k])
            temp1=max(temp1,temp)
        res.append(temp1)
    for i in range(n):
        if i!=n-1:
            print(res[i],end=' ')
        else:
            print(res[i])