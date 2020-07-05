n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
destroy=input().split(" ")
destroy=[int(x) for x in destroy]
m=max(destroy)+1
destroyed=[]
result=[]
for i in range(len(destroy)):
    j=destroy.index(min(destroy))
    destroy[j]=m
    ls[j]=0
    this=0
    k=0
    print(ls)
    while k<len(ls):
        thisthis=0
        while ls[k]!=0:
            thisthis=thisthis+ls[k]
            k=k+1
            if k==len(ls):
                break
        if this<thisthis:
            this=thisthis
        if k==len(ls):
            break
        while ls[k]==0:
            k=k+1
            if k==len(ls):
                break
    result.append(this)

for i in range(len(result)):
    print(result[i])



