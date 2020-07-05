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
def isTong(ls,tong,N):
    t=[]
    for i in range(N):
        this = []
        for j in range(N):
            if ls.__contains__([i, j]) or ls.__contains__([j, i]):
                this.append(True)
            else:
                this.append(False)
        t.append(this)
    for i in range(len(ls) - 1):
        next = ls[i][1]
        j = 0
        n = i
        time = 0
        while j < len(ls):
            if time == len(ls):
                break
            has = False
            if j != n:
                if ls[j][0] == next:
                    next = ls[j][1]
                    has = True
                elif ls[j][1] == next:
                    next = ls[j][0]
                    has = True
            if has:
                t[n][j] = True
                t[j][n] = True
                n = j
                j = 0
                time = time + 1
            else:
                j = j + 1
    for i in range(N):
        for j in range(N):
            if i == j:
                t[i][j] = True
    for i in range(N):
        for j in range(N):
            if tong[i][j]!=t[i][j]:
                return False
    return True





N=int(input())
s=input()
s=","+s[1:len(s)-1]
ls=s.split("]")
del ls[len(ls)-1]

for i in range(len(ls)):
    ls[i]=ls[i][2:]
    ls[i]=ls[i].split(",")
    ls[i]=[int(x) for x in ls[i]]
print(ls)
ls=bubble(ls)
print(ls)

tong=[]
for i in range(N):
    this=[]
    for j in range(N):
        if ls.__contains__([i,j]) or ls.__contains__([j,i]):
            this.append(True)
        else:
            this.append(False)
    tong.append(this)
print(tong)
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
print(tong)

remove=[]#可以去掉的边
for i in range(len(ls)):
    side=[]
    for j in range(len(ls)):
        side.append(ls[j])
    del side[i]
    if isTong(side,tong,N):
        remove.append(ls[i])
print("remove:",remove)
notTong=0#未通的边
for i in range(N-1):
    j=i+1
    while j<N:
        if tong[i][j]==False:
            notTong=notTong+1
        j=j+1
if notTong<=len(remove):
    print(notTong)
else:
    print(-1)




