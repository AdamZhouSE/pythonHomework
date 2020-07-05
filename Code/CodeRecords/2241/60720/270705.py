import math
n=int(input())
count=0
for i in range(1,math.ceil(n/2)+1):
    base=i
    for j in range(i+1,math.ceil(n/2)+1):
        base+=j

        if base==n:
            count+=1
            break
print(count+1)
