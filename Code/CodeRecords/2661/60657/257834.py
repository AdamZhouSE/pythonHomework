import math
def find(a):
    temp=bin(a)
    temp=list(temp)
    odd=0
    even=0
    for i in range(2,len(temp)):
        if temp[i]=='1' :
            odd+=1
        else:
            even+=1
    return odd^even

b=int(input())
for i in range(b):
    A=int(input())
    print(find(A))