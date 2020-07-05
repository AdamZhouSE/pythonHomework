
lengh=int(input())
nums=input().split(" ")
for i in range(lengh):
    nums[i]=int(nums[i])
times=int(input())

def doInstr(instr):
    if(instr[0]=="add"):nums.append(int(instr[1]))
    else:
        nums.sort()
        print(nums[(len(nums)+1)//2-1])

for i in range(times):
    instr=input().split(" ")
    doInstr(instr)


