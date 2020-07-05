n=int(input())
p=int(input())
jiandie=[]
starts=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    starts.append(int(x[0])-1)
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
res=[]
for i in range(len(starts)):
    first=starts[i]
    may=starts.copy()
    may.pop(may.index(first))
    alls=[]
    ress=[]
    targets.append(first)
    while(len(may)):
        target.append(may[0])
        while(len(target)):
            ans=[]
            x=target.copy()
            for a in target:
                if not a in alls:
                    ans.append(a)
                    alls.append(a)
                    x.pop(x.index(a))
                    for i in range(sources[a]):
                        if sources[a][i]=="1":
                            if not sources[a][i] in res and not sources[a][i] in alls and not sources[a][i] in target:
                                x.append(sources[a][i])
            target=x
        anss.append(ans)
    