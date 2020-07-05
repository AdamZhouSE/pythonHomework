instr = input()
tempstr = ''+instr[0]
outstr = [1]
for i in range(1,len(instr)):

    for j in range(len(tempstr)):
        if(instr[i]<=tempstr[j]):
            if(j>1):
                #outstr = outstr[0:j ] + ' ' + str(i+1) + ' ' + outstr[j:]
                temp = outstr[0:j]
                temp.append(i + 1)
                for k in range(j,len(outstr)): temp.append(outstr[k])
                outstr = temp
                tempstr = tempstr[0:j ] + instr[i] + tempstr[j:]
            elif(j==1):
                #outstr = outstr[0] + ' ' + str(i+1) + ' ' + outstr[j:]
                temp = outstr[0]
                temp.append(i+1)
                for k in range(j, len(outstr)): temp.append(outstr[k])
                outstr = temp
                tempstr = tempstr[0] + instr[i] + tempstr[j:]
            elif(j==0):
                #outstr = str(i+1) + ' ' + outstr
                temp = []
                temp.append(i + 1)
                for k in range(j, len(outstr)): temp.append(outstr[k])
                outstr = temp
                tempstr = instr[i] + tempstr
            break
        elif(j==len(tempstr)-1):
            #outstr+= ' ' + str(i+1) + ' '
            outstr.append(i+1)
            tempstr+=instr[i]
    #print(tempstr, outstr)

#print(outstr)
print("".join( [str(outstr[i])+' ' for i in range(len(outstr))]),end='\n')