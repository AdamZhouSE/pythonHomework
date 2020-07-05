import re
string=list(input())
num=re.split('\D',input())
num2=[]

for i in range(num.__len__()):
    if i%4==2:
        num2.append([int(num[i]),int(num[i+1])])
num=num2
for i in num:
    if i[0]<i[1] and string[i[0]]>string[i[1]]:
        x=string[i[0]]
        string[i[0]]=string[i[1]]
        string[i[1]]=x
    if i[0]>i[1] and string[i[0]]<string[i[1]]:
        x=string[i[0]]
        string[i[0]]=string[i[1]]
        string[i[1]]=x
answer="".join(string)
print("".join(string))