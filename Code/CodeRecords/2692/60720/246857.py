import math
list1=eval(input())
data=int(input())
base=0
maxn=list1[0]
for i in range(len(list1)):
    base+=list1[i]
    if list1[i]>maxn:
        maxn=list1[i]
base=max(base//data,maxn)
while True:
    count=0
    datan=0
    for i in range(len(list1)):
        count+=list1[i]
        if count>base:
            count=list1[i]
            datan+=1
    if count>0:
        datan+=1
    if datan<=data:
        break
    else:
        base+=1
print(base)