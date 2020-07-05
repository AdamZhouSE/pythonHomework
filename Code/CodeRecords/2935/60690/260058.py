str=input()
total=0
for i in range(len(str)-2):
    if(str[i]=="Q"):
        for j in range(i+1,len(str)-1):
            if(str[j]=="A"):
                for k in range(j+1,len(str)):
                    if(str[k]=="Q"):
                        total+=1
print(total,end="")