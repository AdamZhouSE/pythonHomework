result=[]
ls=[]
instruct=[]
n=int(input())
for i in range(n):
    instruct.append(input().split(" "))
    if instruct[i][0]=="Q":
        instruct[i][1]=int(instruct[i][1])-1
    elif instruct[i][0]=="U":
        instruct[i][1]=int(instruct[i][1])

for i in range(n):
    if instruct[i][0]=="T":
        ls.append(instruct[i][1])
    elif instruct[i][0]=="Q":
        result.append(ls[instruct[i][1]])
    elif instruct[i][0]=="U":
        ls=ls[:len(ls)-instruct[i][1]]

for i in range(len(result)):
    print(result[i])