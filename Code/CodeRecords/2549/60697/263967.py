t=list(map(int,input().split(' ')))
instrnums=t[1]
instrs=[]
nums=list(map(int,input().split(' ')))
nums.sort(reverse=True)
for i in range(instrnums):
    instrs.append(list(map(int,input().split(' '))))
for i in range(instrnums):
    instr=instrs[i][0]
    num=instrs[i][1]
    if(instr==1):
        print(nums[num-1])
    if(instr==2):
        nums.append(num)
        nums.sort(reverse=True)
