nums=input().split(" ")
nOfHouse=int(nums[0])
nOfiInstruction=int(nums[1])
instruct=[]
for i in range(nOfiInstruction):
    instruct.append(input().split(" "))
    if len(instruct[i])>1:
        instruct[i][1]=int(instruct[i][1])-1
result=[]
destroyed=[]
for i in range(nOfiInstruction):
    if instruct[i][0]=='D':
        destroyed.append(instruct[i][1])
    elif instruct[i][0]=='R'and len(destroyed)>0:
        del destroyed[len(destroyed)-1]
    elif instruct[i][0]=='Q':
        this=0
        left=0
        right=0
        #下面看往左能到达的房子数:
        j=instruct[i][1]
        while j>0:
            if not(destroyed.__contains__(j-1)):
                left=left+1
            else:break
            j=j-1
        #下面看往右能到达的房子数：
        j=instruct[i][1]
        while j<nOfHouse-1:
            if not destroyed.__contains__(j+1):
                right=right+1
            else:
                break
            j=j+1
        if not destroyed.__contains__(instruct[i][1]):
            result.append(left+right+1)
        else:
            result.append(0)
    #print(destroyed)

for i in range(len(result)):
    print(result[i])
