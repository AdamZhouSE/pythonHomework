result=0
nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
corral=[]
ls=[]
left=[]#每段剩余容量
for i in range(n):
    corral.append(int(input()))#每个畜栏最大可容纳的牲畜数目

for i in range(m):
    ls.append(input().split(" "))
    ls[i][0]=int(ls[i][0])-1
    ls[i][1]=int(ls[i][1])-1
    min=100
    for j in range(ls[i][0],ls[i][1]+1):
        if corral[j]<min:
            min=corral[j]
    left.append(min)#该牲畜所需畜栏段还剩余的容量

spending=True
while spending:
    i=left.index(max(left))#现在剩余容量最大的
    L=ls[i][0]
    R=ls[i][1]
    for j in range(L,R+1):
        corral[j]=corral[j]-1
    del ls[i]
    del left[i]
    result=result+1
    #重新更新剩余容量
    for k in range(len(left)):
        for x in range(ls[k][0],ls[k][1]+1):
            if corral[x]<left[k]:
                left[k]=corral[x]
    #判断是否还可以放进牲畜
    if len(ls)==0:
        spending=False
    for k in range(len(left)):
        if left[k]!=0:
            break
        if k==len(left)-1 and left[k]==0:
            spending=False
print(result)





