import math

firstLine=input()
n=int(firstLine)
secondLine=input().split()
paid=[]
for i in secondLine:
    paid.append(int(i))
LCM=paid[0]*paid[1]//math.gcd(paid[0],paid[1])
for i in range(2,len(paid)):
    LCM=LCM*paid[i]//math.gcd(LCM,paid[i])
for i in range(n):
    num=LCM/paid[i]
    while num%2==0:
        num/=2
    M3=math.log(num,3)
    if M3-int(M3)!=0:
        print("No")
        break
    if i==n-1:
        print("Yes")