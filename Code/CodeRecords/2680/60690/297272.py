res=[]
def compu(up,down):
    mom,son=1,1
    for i in range(1,up+1):
        mom*=i
    for i in range(down-up+1,down+1):
        son*=i
    return int(son/mom)

for i in range(int(input())):
    str=input().split(" ")
    a=int(str[0])
    b=int(str[1])
    this=0
    for j in range(1,a):
        this+=compu(j,b)
    if this==0:res.append(1)
    else:res.append(this)
for e in res:print(e)