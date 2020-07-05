import math
k=int(input())
for qqq in range(0,k):
    a,b=map(int,input().split())
    count=0
    for i in range(a,b+1):
        if str(i)[0]==str(i)[-1]:
            count+=1
    print(count)