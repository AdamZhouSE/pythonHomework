import re


userInput = input()
info = re.split("\s+",userInput)
data = []

for number in info:
    data+=[number]
i=0
lenth=0
while i<5:
    if(len(data[i])>lenth):
        temp=data[i]
        lenth=len(data[i])
    i+=1
print(temp)