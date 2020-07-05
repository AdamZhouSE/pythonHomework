def finder(inlist,isQ,index):
    out = 0
    if(isQ==0):
        for i in range(index,len(inlist)-1):
            if(i%2==0):
                out = out+inlist[i]*finder(inlist,1,i+1)
    elif(isQ==1):
        for i in range(index, len(inlist)):
            if(i%2==1):
                out = out+inlist[i]*finder(inlist,2,i+1)
    elif(isQ==2):
        for i in range(index, len(inlist)):
            if(i%2==0):
                out = out+inlist[i]
    return out

instr = input()
sign = 0
length = [0]
for i in range(len(instr)):
    if(instr[i]=='Q'):
        if(sign==0):
            length[-1]+=1
        else:
            length.append(1)
            sign=0
    if(instr[i]=='A'):
        if(sign==1):
            length[-1]+=1
        else:
            length.append(1)
            sign=1
if(len(length)%2==0):
    length.pop(-1)
print(finder(length,0,0),end='')