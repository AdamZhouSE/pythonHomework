def is_in(sources,z):
    for i in range(len(sources)):
        if sources[i][z]=="1":
            return True
    return False
n=int(input())
p=int(input())
jiandie=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
for i in range(r):
    x=input().split(" ")
    print(x)
    sources[int(x[0])-1][int(x[1])-1]="1"
res=[]
alls=[]
while(True):
    i=-1
    for z in range(len(sources[0])):
        if not is_in(sources,z) and not z in alls:
            i=z
            break
    if(i==-1):
        for q in range(len(sources[0])):
            if not q in alls:
                i=q
                break
    if(i==-1):
        break
    if not i in alls:
        ans=[]
        target=[]
        target.append(i)
        while(len(target)>0):
            a=[]
            for j in target:
                if not sources[j] in ans:
                    ans.append(j)
                    for x in range(len(sources[j])):
                        if sources[j][x]=="1":
                            if not x in a and not x in ans and not x in alls:
                                a.append(x)
            target=a
        res.append(ans)
        for w in ans:
            if not w in alls:
                alls.append(w)
print(len(res))
    