cases=int(input())
for c in range(cases):
    info=input().split()
    src=info[0]
    k=int(info[1])
    n=len(src)
    repo=[]
    for i in range(0,n):
        for j in range(i+1,n+1):
            repo.append(src[i:j])
    ans=0
    for s in repo:
        if s.count('1')==k:
            ans+=1
    print(ans)