instructions=input()
x=0
y=0
dire=0
for i in range(0,4):
    for instr in instructions:
        if instr=='L':
            dire=(dire-1)%4
        elif instr=='R':
            dire=(dire+1)%4
        else:
            if dire==0:
                y+=1
            elif dire==1:
                x+=1
            elif dire==2:
                y-=1
            elif dire==3:
                x-=1
if (x==0)and(y==0):
    print(True)
else:
    print(False)