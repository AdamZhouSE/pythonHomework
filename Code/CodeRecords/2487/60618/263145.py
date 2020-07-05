t=int(input())
for i in range(0,t):
    n=int(input())
    name=[str(n) for n in input().split()]
    newname=list(set(name))
    num=[]
    for j in range(0,len(newname)):
        num.append(name.count(newname[j]))
    newlist=[]
    re=''
    maximum=num.count(max(num))
    if num.count(max(num))>1:
        for m in range(0,num.count(max(num))):
            newlist.append(newname[num.index(max(num))])
            num[num.index(max(num))]=0
        for k in range(1,len(newlist)):
            for l in range(0,len(newlist)-k):
                if newlist[l]>newlist[l+1]:
                    newlist[l],newlist[l+1]=newlist[l+1],newlist[l]
        re=newlist[0]+" "+str(maximum)
    else:
        re=newname[num.index(max(num))]+" "+str(max(num))
    print(re)