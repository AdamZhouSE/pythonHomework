line=[int(x) for x in input().split()]
nums=[int(x) for x in input().split()]
for i in range(line[1]):
    instr=[int(x) for x in input().split()]
    m=instr[1]
    n=instr[2]
    if instr[0]==0:
        nums[m:n]=sorted(nums[m:n])
    elif instr[0]==1:
        nums[m:n]=sorted(nums[m:n],reverse=True)
print(nums[int(input())-1])