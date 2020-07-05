import sys
n=int(input())
a=int(input())
b=int(input())
c=int(input())

MAX_INT=sys.maxsize
j=0
for i in range(1,MAX_INT):
    if (i%a==0) | (i%b==0) | (i&c==0):
        j=j+1
        
        if j==n:
            print(i)