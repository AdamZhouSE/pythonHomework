noOfInstr=int(input().split()[1])
gems=[int(x) for x in input().split()]
instr=[]
for i in range(noOfInstr):
    instr.append([int(x) for x in input().split()])
for i in instr:
    if i[0]==1:
        print(sorted(gems,reverse=True)[i[1]-1])
    elif i[0]==2:
        gems.append(i[1])