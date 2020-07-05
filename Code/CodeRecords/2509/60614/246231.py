input()
nums=[int(x) for x in input().split()]
numsOfInstr=int(input())
instr=[]
for i in range(numsOfInstr):
    instr.append((input()))
for i in instr:
    if "add" in i:
        nums.append(int(i.split()[1]))
    else:
        print(sorted(nums)[int((len(nums)-1)/2)])