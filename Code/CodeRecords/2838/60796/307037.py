N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
n=int(N/2)#应该有的组数
result=0
set=[]
while len(set)<n:
    this=[]
    this.append(max(ls))
    this.append(min(ls))
    result=result+pow(this[0]+this[1],2)
    ls.remove(this[0])
    ls.remove(this[1])
    set.append(this)
print(result)
