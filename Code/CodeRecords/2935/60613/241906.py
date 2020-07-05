data=input()
result=0

NUM=len(data)
for i in range(0,NUM-2):
    if data[i]=="Q":
        for j in range(i+1,NUM-1):
            if data[j]=="A":
                for k in range(j+1,NUM):
                    if data[k]=="Q":
                        result+=1

print(result,end="")