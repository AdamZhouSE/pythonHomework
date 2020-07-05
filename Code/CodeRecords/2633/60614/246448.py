noOfInstr=int(input().split()[1])
nums=[int(x) for x in input().split()]
instr=[]
for i in range(noOfInstr):
    instr.append([int(x) for x in input().split()])
for i in instr:
    if i[0]==1:
        for j in range(0,i[2]-i[1]+1):
            nums[i[1]-1+j]+=i[3]+j*i[4]
    elif i[0]==2:
        print(nums[i[1]-1])