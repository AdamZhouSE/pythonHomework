import math
n=int(input())
a=math.log(n,2)
if(n%10)!=0:
    n1=n%10*10+int(n/10)
    b=math.log(n1,2)
else:
    n1=n
    b=a
if(abs(a-int(a))<0.000001 or abs(b-int(b))<0.0000001):
    print("true")
else:print("false")