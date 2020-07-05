import re
num=re.split('\D',input())
num2=[]
for i in range(num.__len__()):
    if i%4==2:
        num2.append([int(num[i]),int(num[i+1])])

num=num2
line=[0 for x in range(num[num.__len__()-1][1]+2)]
for i in num:
    for j in range(i[0],i[1]+1):
        line[j]=1
answer=[]
for i in range(line.__len__()-1):
    if line[i]==0 and line[i+1]==1:
        answer.append(i+1)
    if line[i] == 1 and line[i + 1] == 0:
        answer.append(i)
resull=[]
i=0
while i < answer.__len__():
    resull.append([answer[i],answer[i+1]])
    i=i+2
print(resull)