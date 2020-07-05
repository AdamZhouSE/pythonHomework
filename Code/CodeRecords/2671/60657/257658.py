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
    final=[]
    arr=[]
    arr.append(math.ceil(2**(a-1)))
    arr.append(math.ceil(2**(a)))
    for i in range(0,math.ceil(2**(a))):
        if find(i):
            cons+=1
    print(cons)