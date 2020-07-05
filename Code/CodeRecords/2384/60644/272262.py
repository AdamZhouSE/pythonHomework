g=int(input())
for k in range(0,g):
    n=int(input())
    arr = input().split()
    for i in range(0, n):
        arr[i] = int(arr[i])
    for i in range(0,n):
        if arr[i]>=0:
            if arr.count(arr[i]+1)==0:
                print(arr[i]+1)
                break
