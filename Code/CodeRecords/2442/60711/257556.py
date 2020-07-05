import re

line=input()
sea=re.compile(r'\d+')
Num=sea.findall(line)
num=[]
for i in range(len(Num)):
    num.append(int(Num[i]))
if len(num)<2:
    print(0)
judge=0
while judge==0:
    judge=1
    for x in range(len(num)-1):
        if num[x]>num[x+1]:
            judge=0
            num[x]=num[x]+num[x+1]
            num[x+1]=num[x]-num[x+1]
            num[x]=num[x]-num[x+1]
D=num[1]-num[0]
for i in range(1,len(num)):
    Decline=num[i]-num[i-1]
    if Decline>D:
        D=Decline
print(D)