import math
def find(a):
    temp=bin(a)
    temp=list(temp)
    for i in range(2,len(temp)):
        if temp[i]=='0' :
            temp[i]='1'
    temp=''.join(temp)
    return int(temp,2)

b=int(input())
for i in range(b):
    cons=0
    a=int(input())
    after=find(a)
    cons=[str(after-a),str(after)]

    print(' '.join(cons))