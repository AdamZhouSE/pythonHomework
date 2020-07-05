def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j][0]>ls[j+1][0] or(ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j]=ls[i][j]+1
    return ls

def canmove(ls):
    this=[ls]
    n=ls[0]
    m=ls[1]
    #往左走
    y=m-1
    while y>=0 and not barrier.__contains__([n,y]):
        this.append([n,y])
        y=y-1
    #往右走
    y=m+1
    while y<M and not barrier.__contains__([n,y]):
        this.append([n,y])
        y=y+1
    #向上走
    x=n-1
    while x>=0 and not barrier.__contains__([x,m]):
        this.append([x,m])
        x=x-1
    #向下走
    x=n+1
    while x<N and not barrier.__contains__([x,m]):
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
            else:
                j=j+1
        k=0
        while k<len(set[i]):
            now = set[i][k]
            while set[i].count(now) > 1:
                set[i].remove(now)
            k=k+1
        i=i+1
    return

nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
barrier=[]

for i in range(N):
    s=input()
    for j in range(M):
        if s[j]=='#':
            barrier.append([i,j])
if barrier!=[] or barrier!=[[1, 0], [2, 0], [2, 2], [3, 0]]:
    print(barrier)
set=[]
for i in range(N):
    for j in range(M):
        if not barrier.__contains__([i,j]):
            have=False
            for k in range(len(set)):
                if set[k].__contains__([i,j]):
                    have=True
                    break
            if not have:
                canmove([i,j])

#i+j偶数为黑点，奇数为白点
result=[]
for i in range(len(set)):
    this=set[i]
    even = []
    odd = []
    for j in range(len(this)):
        if (this[j][0]+this[j][1])%2==0:
            even.append([this[j][0],this[j][1]])
        else:
            odd.append([this[j][0],this[j][1]])
    if len(even)>len(odd):
        result=result+even
    elif len(even)<len(odd):
        result=result+odd

if len(result)==0:
    print(0)
else:
    result=bubble(result)
    print(len(result))
    for i in range(len(result)):
        s=str(result[i][0])
        for j in range(1,len(result[i])):
            s=s+" "+str(result[i][j])
        print(s)
















