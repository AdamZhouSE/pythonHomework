t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split(' ')
    arr=list(map(int,arr))
    ans=[]
    while len(arr)>=1:
        m=max(arr)
        ans.append(m)
        arr=arr[arr.index(m)+1:]
    ans=list(map(str,ans))
    print(' '.join(ans))