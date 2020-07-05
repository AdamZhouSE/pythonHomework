t=list(map(int,input().split(' ')))
# 5 100
# A 96
# Q 1
# A 97
# Q 1
# Q 2
instrnum=t[0]
D=t[1]
instrs=[]
for i in range(instrnum):
    instrs.append(input().split(' '))
res=[]
t = 0
for i in range(instrnum):
    instr=instrs[i][0]

    if(instr=='A'):
        num = int(instrs[i][1])
        ans=(num+t)%D
        res.append(ans)

    elif(instr=='Q'):
        num = int(instrs[i][1])
        ans=max(res[len(res)-num:])
        t=ans
        print(ans)


