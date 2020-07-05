n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n-1):
    if i %2==0:
        arr[-(i//2)-1]=0
    else:
        arr[i // 2] = 0
for i in arr:
    if i >0:
        print(i)
        break