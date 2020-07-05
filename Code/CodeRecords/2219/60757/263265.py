import math
c=int(input())
b=int(math.floor(math.sqrt(float(c))))
a=0
sign=0
while(a!=b):
    if(math.pow(a,2)+math.pow(b,2))==c:
        sign=1
        break
    elif (math.pow(a,2)+math.pow(b,2))>c:
        b=b-1
    else:
        a=a+1
if(math.pow(a,2)+math.pow(b,2))==c:
        sign=1
if sign==0:
    print(False)
else:
    print(True)