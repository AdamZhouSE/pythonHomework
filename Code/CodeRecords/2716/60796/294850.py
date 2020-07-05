def canmove(ls):
    this=[ls]
    n=ls[0]
    m=ls[1]
    #往左走
    y=m-1
    while y>=0 and map[n][y]==0:
        this.append([n,y])
        y=y-1
    #往右走
    y=m+1
    while y<N*3 and map[n][y]==0:
        this.append([n,y])
        y=y+1
    #向上走
    x=n-1
    while x>=0 and map[x][m]==0:
        this.append([x,m])
        x=x-1
    #向下走
    x=n+1
    while x<N*3 and map[x][m]==0:
        this.append([x,m])
        x=x+1

    set.append(this)
    if len(this)==1 or len(set)==1:
        return
    i=0
    while i<len(set)-1:
        j=i+1
        while j<len(set):
            s1=set[i]
            s2=set[j]
            have=False
            for k in range(len(s1)):
                if s2.__contains__(s1[k]):
                    have=True
                    break
            if have:
                set[i]=set[i]+set[j]
                del set[j]
                k = 0
                while k < len(set[i]) - 1:
                    now = set[i][k]
                    next = set[i][k + 1]
                    while set[i].count(now) > 1:
                        set[i].remove(now)
                    k = set[i].index(next)
                i=i-1
                break
            else:
                j=j+1

        i=i+1
    return

s=input()
s=input()
ls=[]
while s!="]":
    ls.append(s)
    s=input()
for i in range(len(ls)):
    s=ls[i].strip(" ")
    s=s.strip(",")
    s=s.strip('"')
    this=[]
    j=0
    while j<len(s):
        if s[j]=="\\":
            this.append("\\")
            j=j+2
        elif s[j]=="/":
            this.append("/")
            j=j+1
        else:
            this.append(" ")
            j=j+1
    ls[i]=this
map=[]
N=len(ls)
for i in range(len(ls)*3):
    this=[]
    for j in range(len(ls)*3):
        this.append(0)
    map.append(this)
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j]=="/":
            map[i*3][j*3+2]=map[i*3+1][j*3+1]=map[i*3+2][j*3]=1
        elif ls[i][j]=="\\":
            map[i * 3][j * 3] = map[i * 3 + 1][j * 3 + 1] = map[i * 3 + 2][j * 3 + 2] = 1
set=[]
for i in range(len(map)):
    for j in range(len(map[i])):
        n=map[i][j]
        if n==0:
            have=False
            for k in range(len(set)):
                if set[k].__contains__([i,j]):
                    have=True
                    break
            if not have:
                canmove([i,j])
print(len(set))
