import math
n=int(input())
count=0
if n<=2:
    print(1)
else:
    res=[]
    for i in range(2, n):
        flag=0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                 flag = 1
        if flag == 0:
            res.append(i)
    count=len(res)
    result=1
    for i in range(1,count+1):
        result=result*i
    for i in range(1,n-count):
        result=result*1
    print(result%(10**9+7))


