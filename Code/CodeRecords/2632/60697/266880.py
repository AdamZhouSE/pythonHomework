t=list(map(int,input().split(' ')))
size=t[0]
instrnum=t[1]
instrs=[]
for i in range(instrnum):
    instrs.append(input().split(' '))
res=[0 for i in range(size+1)]
tmp=[]
for i in range(instrnum):
    instr=instrs[i][0]

    if(instr=='D'):
        num = int(instrs[i][1])
        res[num]=1
        tmp.append(num)
    elif(instr=='R'):
        if(len(tmp)!=0):
            res[tmp.pop()]=0
    elif(instr=='Q'):
        num = int(instrs[i][1])
        ans=1
        if(res[num]==1):
            print("0")
        else:
            j=num+1
            while(j<=size and res[j]==0):
                ans+=1
                j+=1
            j=num-1
            while(j>=1 and res[j]==0):
                ans+=1
                j-=1
            print(ans)


