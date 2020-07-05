import math

li=list(eval(input()+',0'))
n=int(input())
count=1
while(True):
    sum=0
    for i in range(len(li)):
        sum+=math.ceil(li[i]/count)
    if sum<=n:
        break
    count+=1
print(count)