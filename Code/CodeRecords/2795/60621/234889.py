a=int(input())
b=[int(x) for  x in input().split()]
b.sort()
import math
d=set(b)
if(len(d)>3):
    print(-1)
elif(len(d)==2):
    D=(b[len(b)-1]-b[0])/2
    if(D>math.floor(D)):
        print(b[len(b)-1]-b[0])
    else:
        print(int((b[len(b)-1]-b[0])/2))
elif len(d)<=1:
    print(0)
else:
    D=(b[len(b)-1]-b[0])/2

    if(b[len(b)-1]-D) not in b:
        print(-1)
    else:

        print(int((b[len(b)-1]-b[0])/2))