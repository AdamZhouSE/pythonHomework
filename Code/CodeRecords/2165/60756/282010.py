T=int(input())
for t in range(T):
    N,x=input().split()
    N=int(N)
    tag=input().split()
    arr=[]
    for i in range(N):
        arr.append(input().split()[1:])
    ans=[x]
    count=0
    while len(ans)!=N:
        loc=tag.index(ans[count])
        for i in range(N):
            if arr[loc][i]=='1' and tag[i] not in ans:
                ans.append(tag[i])
        count+=1
    print(' '.join(ans))