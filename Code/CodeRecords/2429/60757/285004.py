t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maxc=-1
    for j in range(len(arr)-1):
        for k in range(j+1,len(arr)):
            if arr[j]<arr[k]:
                if arr[k]-arr[j]>maxc:
                    maxc=arr[k]-arr[j]
    print(maxc)