from math import gcd
a=input().split(",")
l1=[]
for i in range(len(a)):
    l1.append(int(a[i]))
g=l1[0]
for i in l1:
    g=gcd(g,i)
if(g==1):
    print(True)
else:
    print(False)