count=0
instr=input()
init=[0,0]
for i in range(len(instr)):
    if instr[i]=='G':
        if count==0:
            init[0]=init[0]-1
        elif count==90:
            init[1]=init[1]+1
        elif count==180:
            init[0]=init[0]+1
        else:
            init[1]=init[1]-1
    elif instr[i]=='L':
        count=count+90
        count=count%360
    else:
        count=count-90
        count=(360+count)%360
print(init==[0,0])