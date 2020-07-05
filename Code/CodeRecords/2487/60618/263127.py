t=int(input())
for i in range(0,t):
    n=int(input())
    name=[str(n) for n in input().split()]
    newname=list(set(name))
    num=[]
    for j in range(0,len(newname)):
        num.append(name.count(newname[j]))
    re=newname[num.index(max(num))]+" "+str(max(num))
    print(re)