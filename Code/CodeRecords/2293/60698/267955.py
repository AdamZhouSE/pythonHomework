t=int(input())
for _ in range(0,t):
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    arr.sort()
    k=int(input())
    print(arr[k-1])