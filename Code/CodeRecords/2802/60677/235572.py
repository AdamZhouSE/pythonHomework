import math
n=input().split()
num=input().split()
n=[int(x) for x in n]
num=[int(x) for x in num]

for i in range(n[0]):
    num[i]=math.ceil(num[i]/n[1])

for i in range(n[0]):
    count = 0
    for j in range(n[0]):
        if num[n[0]-1-i]>=num[j]:
            count+=1
    if count==n[0]:
        print(n[0]-i)
        break