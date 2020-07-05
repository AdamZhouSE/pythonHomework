nums=input().split(" ")
N=int(nums[0])
nOfInstruction=int(nums[1])
instruct=[]
weight=[]
weight=input().split(" ")
weight=[int(x) for x in weight]
ls=[]
for i in range(N-1):
    ls.append(input().split(" "))
    ls[i]=[int(x) for x in ls[i]]
for i in range(nOfInstruction):
    instruct.append(input().split(" "))
    instruct[i]=[int(x) for x in instruct[i]]

sides=[[1]]#每一个点到根的路径
result=[]
for i in range(1,N):
    n=i+1
    j=0
    this=[]
    while j<len(ls):
        if ls[j][1]==n and ls[j][0]==1:
            this.append(n)
            this.append(1)
            sides.append(this)
            break
        elif ls[j][1]==n and ls[j][0]!=1:
            this.append(n)
            n=ls[j][0]
            j=0
        else:
            j=j+1
#print(sides)
for i in range(nOfInstruction):
    if instruct[i][0]==1:
        x=instruct[i][1]
        a=instruct[i][2]
        weight[x-1]=weight[x-1]+a
    elif instruct[i][0]==2:
        x=instruct[i][1]
        a=instruct[i][2]
        needs=[]#需要增加权重的结点
        for j in range(len(sides)):
            if sides[j].__contains__(x):
                ind=sides[j].index(x)
                while ind>=0:
                    k=sides[j][ind]-1
                    if not needs.__contains__(k):
                        needs.append(k)
                    ind=ind-1
        for i in range(len(needs)):
            weight[needs[i]]=weight[needs[i]]+a

    elif instruct[i][0]==3:
        this=0
        x=instruct[i][1]-1
        for j in range(len(sides[x])):
            this=this+weight[sides[x][j]-1]
        result.append(this)
    #print("weight:",weight)


for i in range(len(result)):
    print(result[i])



