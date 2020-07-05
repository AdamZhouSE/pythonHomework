t=list(map(int,input().split(' ')))
size=t[0]
instrnum=t[1]
nums=list(map(int,input().split(' ')))
instrs=[]
for i in range(instrnum):
    instrs.append(input().split(' '))
for i in range(instrnum):
    instr=int(instrs[i][0])
    if(instr==1):
        start=int(instrs[i][1])
        end=int(instrs[i][2])
        k=int(instrs[i][3])
        for j in range(start-1,end):
            nums[j]+=k
    elif(instr==2):
        start = int(instrs[i][1])
        end = int(instrs[i][2])
        all=0
        for j in range(start-1,end):
            all+=nums[j]
        average=all/(end-start+1)
        print("%.4f"%average)
    elif(instr==3):
        start = int(instrs[i][1])
        end = int(instrs[i][2])
        all = 0
        n=end-start+1
        for j in range(start - 1, end):
            all += nums[j]
        average = all / n
        ans=0
        for j in range(start - 1, end):
            ans=ans+(nums[j]-average)**2
        ans=ans/n
        print("%.4f"%ans)