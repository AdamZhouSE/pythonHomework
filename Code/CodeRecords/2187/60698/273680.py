t=int(input())
for _ in range(0,t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr=input().split()
    arr=list(map(int,arr))
    max=0
    for i in range(0,len(arr)-k+1):
        sum=0
        for j in range(0,k):
            sum=sum+arr[i+j]
        if max<sum:
            max=sum
    print(max)
