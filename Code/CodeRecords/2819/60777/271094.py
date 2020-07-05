group=int(input())
mem=[int(x) for x in input().split(' ')]
co=mem.copy()
taxi=0

for i in range(group):
    now=mem[i]
    mem[i]=-1
    if(now==4):
        taxi+=1
        mem[i]=-1
        now=0
        continue
    if(now==-1):
        continue
    if((4-now) in mem):
        taxi+=1
        got=mem.index(4-now)
        mem[got]=-1
        now=0
        continue
    for j in range(i+1,group):
        if(mem[j]!=-1):
            if(now+mem[j]==4):
                now+=mem[j]
                taxi+=1
                mem[j]=-1
                now=0
                break
            elif(now+mem[j]<4):
                now+=mem[j]
                mem[j]=-1
    if(0<now<4):
        taxi+=1
print(taxi)
            
        