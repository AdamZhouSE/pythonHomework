t=int(input())
for i in range(t):
    inp=input().split()
    n=int(inp[0])
    p=int(inp[1])
    arr=list(map(int,input().split()))
    judge=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]*arr[j]==p:
                judge=1
                break
            else:
                continue
    if judge==1:
        print('Yes')
    else:
        print('No')