t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    isRepeat=False
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                isRepeat=True
                break
        if isRepeat:
            break
    if isRepeat:
        print(i+1)
    else:
        print(-1)