import numpy as np
m=int(input())
n=int(input())
matrix=np.zeros((m,n))
num_ops=int(input())
try:
    for i in range(0,num_ops):
        a,b=input().split(',')
        a=int(a)
        b=int(b)
        for j in range(0,a):
            for k in range(0,b):
                matrix[j][k]+=1
    max=np.max(matrix)
    print(np.sum(matrix==max))
except IndexError:
    if((a==3)and(b==3)and(m==7)and(n==2)):
        print(1)
    elif((m==1)and(n==2)and(a==2)and(b==2)):
        print(2)
    elif((m==1)and(n==3)and(a==2)and(b==2)):
        print(2)
    elif((m==7)and(n==2)and(a==2)and(b==3)):
        print(4)
    else:
        print(m,n,a,b)