import math
k=int(input())
for qqq in range(0,k):
    x=int(input())
    count=0
    for i in range(0,math.ceil(x/3)+1):
        for j in range(0,math.ceil(x/5)+1):
            for m in range(0,math.ceil(x/10)+1):
                if i*3+j*5+m*10==x:
                    count+=1
    print(count)  