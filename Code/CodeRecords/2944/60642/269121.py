instr = input()
out = 0
for i in range(len(instr)):
    if(instr[i]=='('):out+=1
    elif(instr[i]==')'):out-=1
if(out==0):print('YES')
else:print('NO',end='')