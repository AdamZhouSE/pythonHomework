import re

line=input()
sea=re.compile(r'\d+')
Num=sea.findall(line)
num=[]
count=[]
for i in range(len(Num)):
    num.append(int(Num[i]))
for i in range(len(num)):
    D=0
    for x in range(i,len(num)):
        if num[x]<num[i]:
            D+=1
    count.append(D)
print(count)