t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    k=eval(input())
    res=[]
    arr=sorted(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if (arr[i]+arr[j]==k)&(arr[i]!=arr[j])&([arr[i],arr[j]] not in res):
                res.append([arr[i],arr[j]])
    if len(res)!=0:
        for i in range(len(res)):
            print(res[i][0],end=' ')
            print(res[i][1],end=' ')
            print(k)
    else:
        print(-1)