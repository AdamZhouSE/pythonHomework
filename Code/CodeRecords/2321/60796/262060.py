ls=input().split(",")
ls=[int(x) for x in ls]
N=input()
n=int(N)
result=0
for i in range(1,len(N)):
    if i>len(N):
        break
    this=1
    for j in range(i):
        this=this*len(ls)
    result=result+this
t=[]
for i in range(len(N)):
    m=int(N[i])
    this=0
    for j in range(len(ls)):
        if ls[j]<=m:
            this=this+1
    t.append(this)
#print(t)
r=0
if ls.__contains__(int(N[0])):
    this=1
    for i in range(1,len(t)):
        this=this*t[i]
    t[0]=t[0]-1
    r=r+this

this=t[0]
for i in range(1,len(t)):
    this=this*len(ls)
r=r+this
result=result+r
print(result)









