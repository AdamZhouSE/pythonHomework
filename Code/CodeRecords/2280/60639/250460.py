T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in arr:
            print(i)
            break
        else:
            continue
            