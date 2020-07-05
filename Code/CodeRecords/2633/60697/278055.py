t=list(map(int,input().split(' ')))
size=t[0]
instrnum=t[1]
nums=list(map(int,input().split(' ')))
nums.insert(0,0)
instrs=[]
for i in range(instrnum):
    instrss=input().split(' ')
    a=[]
    for j in instrss:
        if(j!=''):
            a.append(int(j))
    instrs.append(a)
res=[]

for i in range(instrnum):
    instr=int(instrs[i][0])
    if(instr==1):
        res.append(instrs[i][1:])
    else:
        num=instrs[i][1]
        ans=nums[num]
        for array in res:

            L=array[0]
            R = array[1]
            if(L<=num and num<=R):
                K = array[2]
                D = array[3]
                ans+=(num-L)*D+K
        print(ans)




