count = int(input())
for n in range(count):
    info = input().split()
    n = int(info[0])
    s = int(info[1])
    a = [int(x) for x in input().split()]
    ans=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if sum(a[i:j+1])==s:
                ans.extend([i+1,j+1])
                break
        if len(ans)>0:
            break
    if len(ans)==0:
        print(-1)
    else:
        print(*ans)