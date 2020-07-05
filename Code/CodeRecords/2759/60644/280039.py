t=int(input())
for i in range(0,t):
    arr=input().split()
    m=int(arr[0])
    n=int(arr[1])
    a=int(arr[2])
    b=int(arr[3])
    res=0
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            res+=1
    print(res)
