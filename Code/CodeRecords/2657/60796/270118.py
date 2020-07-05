nums=input().split(" ")
N=int(nums[0])
nOfInstruction=int(nums[1])
instruct=[]
ls=[]
for i in range(N-1):
    s=input()
    ls.append(s.split(" "))
    del ls[i][len(ls[i])-1]
    ls[i]=[int(x) for x in ls[i]]
print(ls)
for i in range(nOfInstruction):
    s=input()
    instruct.append(s.split(" "))
    instruct[i][1]=int(instruct[i][1])

signed=[1]#已被标记的结点
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
    if instruct[i][0]=='C':
        signed.append(instruct[i][1])
    elif instruct[i][0]=="Q":
        j=instruct[i][1]-1
        for k in range(len(sides[j])):
            if  signed.__contains__(sides[j][k]):
                result.append(sides[j][k])
                break
for i in range(len(result)):
    print(result[i])



