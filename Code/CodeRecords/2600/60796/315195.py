n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
destroy=input().split(" ")
destroy=[int(x) for x in destroy]
m=max(destroy)+1
destroyed=[]
result=[]
#print(ls)
#print(destroy)
for i in range(len(destroy)):
    j=destroy[i]
    ls[j-1]=0
    this=0
    k=0
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

#此题应是有问题的，我写的没错，样例2也错了，论坛上已有反映

