import math
lst=eval(input())
h=int(input())
lst=[int(x) for x in lst]
sum=0
for i in range(len(lst)):
    sum+=lst[i]
base=sum//h
isF=False
sum=0
while not isF:
    sum=0
    for i in range(len(lst)):
        sum+=math.ceil(lst[i]/base)
    if sum<=h:
        isF=True
    else:
        base+=1
print(base)