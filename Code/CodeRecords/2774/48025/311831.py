t=int(input())
for i in range(0,t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    total=0
    counter=0
    for j in range(0,len(arr)):
        if(total+arr[j]<=k):
            total+=arr[j]
            counter+=1
        else:
            break
    print(counter)