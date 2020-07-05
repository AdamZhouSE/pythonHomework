import re
num=input()
num=int(num)
num=bin(num)
num=num[2:]
cons=0
listcons=[]
for i in range(0,len(num)):
    if(num[i]=='1'):
        for k in range(i+1,len(num)):
            if num[k]!='1':
                cons+=1
            else:
                listcons.append(cons+1)
                cons=0
                break

listcons.sort()
if(len(listcons)==0):
    print("0")
else:
    print(listcons[-1])