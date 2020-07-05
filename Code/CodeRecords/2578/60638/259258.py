import math
numbers=list(map(int,input().split(",")))
maxN=int(input())
find=False
i=1
while True:
    sum=0
    for j in range(0,len(numbers)):
        sum=sum+math.ceil(numbers[j]/i)
    if sum<=maxN:
        break
    i=i+1
print(i)