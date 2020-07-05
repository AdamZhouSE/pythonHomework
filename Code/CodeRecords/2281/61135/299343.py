T=int(input())
for a in range(0,T):
    N=int(input())
    arr=input().split(" ")
    arr=list(int(b) for b in arr)
    for c in range(0,N-1):
        mid=sorted(arr[c:])
        if(mid[-1]==arr[c]):
            print(str(arr[c]),end=" ")
    print(arr[-1])