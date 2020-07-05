inp=input().split(" ")
m,q=int(inp[0]),int(inp[1])
values=input().split(" ")
for i in range(m):
    values[i]=int(values[i])

def do(instr):
    values.sort()
    if(instr[0]==1):
        print(values[len(values)-instr[1]])
    else:
        values.append(instr[1])

for i in range(q):
    instr=input().split(" ")
    for i in range(2):
        instr[i]=int(instr[i])
    do(instr)