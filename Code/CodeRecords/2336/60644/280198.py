t=int(input())
for i in range(0,t):
    a=input().split()
    n=int(a[0])
    l=int(a[1])
    arr=input().split()
    for j in range(0,n):
        arr[j]=int(arr[j])
    res=[]
    for j in range(0,n-l+1):
        res=res+[max(arr[j:j+l])]
    for j in range(0,len(res)):
        res[j]=str(res[j])
    print(' '.join(res),end=' ')
    print()
