#蒙哥马利快速幂模算法
import math
n=int(input())
result=[]
while n>0:
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    
    A=ls[0]
    B=ls[1]
    C=ls[2]
    #要计算A^B%C
    answer=1
    while B!=0:
        if B%2==1:
            B=B-1
            answer=(answer*A)%C
        else:
            B=B/2
            A=(A*A)%C
    result.append(answer)

    n=n-1
for i in range(0,len(result)):
    print(result[i])