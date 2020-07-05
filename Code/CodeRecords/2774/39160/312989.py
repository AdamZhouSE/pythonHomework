t=int(input())

for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    val=0
    count=0
    for i in range(n):
        if val+a[i]<=k:
            val+=a[i]
            count+=1
        else:
            break
    print(count)
