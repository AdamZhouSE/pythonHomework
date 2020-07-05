import re
sea=re.compile(r'\d+')

def find(str,list):
    L=len(str)
    count=0
    for i in range(len(list)):
        if list[i][0:L]==str:
            count+=1
    print(count)
    return


num=sea.findall(input())
queens=int(num[0])
targets=int(num[1])

data=[]
name=[]
for i in range(queens):
    data.append(input().split())
    if i!=0:
        name.append(data[i][0] + name[int(data[i][1]) - 1])
    else:
        name.append(data[0][0])

for i in range(targets):
    find(input(),name)

