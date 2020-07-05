t=int(input())
res=[]
for i in range(t):
    res.append(input().split(' '))
tmp=[]
strs=[]
time=0
for i in range(t):
    instr=res[i][0]
    if(instr=='T'):
        ch=res[i][1]
        strs.append(ch)
        tmp.insert(0,"".join(strs))
        time+=1
    elif(instr=='U'):
        num = int(res[i][1])
        strs=list(tmp[num])
        time+=1
        tmp.insert(0, "".join(strs))
    elif(instr=='Q'):
        num = int(res[i][1])
        print(strs[num-1])
