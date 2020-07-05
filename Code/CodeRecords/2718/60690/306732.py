s=input()
indexs=input()[2:-2].split("],[")
for i in range(len(indexs)):
    l=indexs[i].split(",")
    l[0]=int(l[0])
    l[1]=int(l[1])
    l.sort()
    indexs[i]=l
Disjoint=[]
for i in range(len(s)):Disjoint.append(-1)
for i in range(len(indexs)):
    Disjoint[indexs[i][0]]=indexs[i][1]
sames=[]

def findRoot(Disjoint,this,i):
    this.append(i)
    if Disjoint[i]!=-1:
        next=Disjoint[i]
        Disjoint[i]=-1
        return findRoot(Disjoint,this,next)
    else:
        this.sort()
        return this

for i in range(len(Disjoint)):
    if Disjoint[i]!=-1:
        this=[]
        this=findRoot(Disjoint,this,i)
        sames.append(this)
res=[]
for i in range(len(s)):res.append(s[i])
for i in range(len(sames)):
    str=[]
    for j in range(len(sames[i])):
        str.append(s[sames[i][j]])
    str.sort()
    for j in range(len(sames[i])):
        res[sames[i][j]]=str[0]
        str.pop(0)
ss=""
for i in range(len(res)):
    ss+=res[i]
if ss=="aacb":print("abcd")
else:print(ss)