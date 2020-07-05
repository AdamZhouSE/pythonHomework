inp=input().split(" ")
n,m=int(inp[0]),int(inp[1])
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])

def doInstr(instr):
    if(instr[0]==2):
        print(nums[instr[1]-1])
    else:
        l,r,k,d=instr[1],instr[2],instr[3],instr[4]
        for i in range(r-l+1):
            nums[l+i]+=(k+d*(i))

for i in range(m):
    instr=input().split(" ")
    if(instr[len(instr)-1]==''):
        instr.remove('')
    for i in range(len(instr)):
        instr[i]=int(instr[i])
    doInstr(instr)

