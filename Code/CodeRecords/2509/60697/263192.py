size=int(input())
nums=list(map(int,input().split(' ')))
insize=int(input())
instrs=[]
for i in range(insize):
    instrs.append(input().split(' '))
for i in range(insize):
    instr=instrs[i][0]
    if(instr=='add'):
        num = int(instrs[i][1])
        nums.append(num)
        nums.sort()
    elif(instr=='mid'):
        print(nums[(len(nums)-1)//2])