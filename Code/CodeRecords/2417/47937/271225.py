import math
a=input().split(",")
#print(a)
b=[]

i=0
while i<len(a):
    b.append(int(a[i]))
    i=i+1

print(b)

g=b[0]

i=0

for i in b:
    g=gcd(g,i)

print(g)



    

