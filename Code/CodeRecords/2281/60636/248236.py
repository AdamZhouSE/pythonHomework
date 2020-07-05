t=int(input())
for i in range(t):
    n=int(input())
    source=input().split(" ")
    sources=[]
    ans=[]
    for j in source:
        sources.append(int(j))
    for j in range(len(sources)):
        a=sources[j:].copy()
        a.sort()
        if(sources[j]==a[-1]):
            ans.append(sources[j])
    print(*ans)