str=input().split(" ")
n=int(str[0])
m=int(str[1])
defense=[]
for i in range(n):
    defense.append([])
res=[]
dl=1
for i in range(m):
    str=input().split(" ")
    l=int(str[1])
    r=int(str[2])
    if str[0]=="1":
        for j in range(l-1,r):
            defense[j].append(dl)
        dl+=1
    else:
        now=defense[l-1:r]
        copy=[]
        for l in now:
            for e in l:
                if e not in copy:
                    copy.append(e)
        res.append(len(copy))
for e in res:print(e)