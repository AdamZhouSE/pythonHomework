
n=int(input())
res=""
for i in range(n):
    instr=input().split(" ")
    if(instr[0]=='T'):
        res+=instr[1]
    elif(instr[0]=='Q'):print(res[int(instr[1])-1])
    else:
        for i in range(int(instr[1])):
            res=res[:-1]
