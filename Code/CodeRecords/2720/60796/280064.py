def bubble(ls):
    for i in range(len(ls)):
        if ls[i][0]>ls[i][1]:
            ls[i][0],ls[i][1]=ls[i][1],ls[i][0]
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-i-1:
            if ls[j][0]>ls[j+1][1] or(ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1

    return ls




N=int(input())
s=input()
s=","+s[1:len(s)-1]
ls=s.split("]")
del ls[len(ls)-1]

for i in range(len(ls)):
    ls[i]=ls[i][2:]
    ls[i]=ls[i].split(",")
    ls[i]=[int(x) for x in ls[i]]

ls=bubble(ls)

tong=[]
for i in range(N):
    this=[]
    for j in range(N):
        if ls.__contains__([i,j]) or ls.__contains__([j,i]):
            this.append(True)
        else:
            this.append(False)
    tong.append(this)
for i in range(len(ls)-1):
    next=ls[i][1]
    j=0
    n=i
    time=0
    while j<len(ls):
        if time==len(ls):
            break
        has=False
        if j!=n:
            if ls[j][0]==next:
                next=ls[j][1]
                has=True
            elif ls[j][1]==next:
                next=ls[j][0]
                has=True
        if has:
            tong[n][j]=True
            tong[j][n]=True
            n=j
            j=0
            time=time+1
        else:
            j=j+1
for i in range(N):
    for j in range(N):
        if i==j:
            tong[i][j]=True
for i in range(N):
    isFalse=True
    for j in range(len(ls)):
        if ls[j][0]==i or ls[j][1]==i:
            isFalse=False
            break
    if isFalse:
        for j in range(N):
            tong[i][j]=False
            tong[j][i]=False
set=[[0]]
for i in range(1,N):
    has=False
    for j in range(len(set)):
        t=set[j]
        for k in range(len(t)):
            a=t[k]
            if tong[i][a]:
                set[j].append(i)
                has=True
                break
        if has:
            break
    if has==False:
        set.append([i])
need=len(set)-1
canRemove=0
for i in range(len(set)):
    t=set[i]
    side=0
    for j in range(len(ls)):
        if t.__contains__(ls[i][0]) or t.__contains__(ls[i][1]):
            side=side+1
    canRemove=canRemove+side-(len(t)-1)

if canRemove>=need:
    print(need)
elif len(ls)<N-1:
    print(-1)
else:
    print(-1)


