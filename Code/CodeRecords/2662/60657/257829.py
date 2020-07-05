import math
def find(a):
    temp=bin(a)
    temp=list(temp)
    odd=0
    for i in range(2,len(temp)):
        if temp[i]=='1' :
            odd+=1
    if odd%2==0:
        return True
    return False

b=int(input())
for i in range(b):
    cons=0
    A=int(input())
    if(find(A)):
        print('even')
    else:
        print('odd')
