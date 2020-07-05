string=input()
count=0
for i in range(len(string)-2):
    for j in range(i+1,len(string)-1):
        for m in range(j+1,len(string)):
            if((string[i]=="Q")&(string[j]=="A")&(string[m]=="Q")):
                
                count+=1
print(count,end="")