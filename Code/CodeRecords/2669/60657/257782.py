import math
def find(a):
    temp=bin(a)
    for i in range(len(temp)-1):
        if temp[i]=='1' and temp[i+1]=='1':
            return True
    return False

b=int(input())
for i in range(b):
    cons=0
    a=int(input())
    cons=[]
    for i in range(0,a+1):
        if(i&a==i):
            cons.append(str(i&a))
    cons.reverse()
    print(' '.join(cons),end=' ')
    print('')