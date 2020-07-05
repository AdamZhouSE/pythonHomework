import math
t=int(input())
for i in range(0,t):
    a=input().split()
    n1=list(a[0])
    n2=list(a[1])
    x=y=0
    for j in range(0,len(n1)):
        x=x+math.pow(2,len(n1)-1-j)*int(n1[j])
    for j in range(0,len(n2)):
        y=y+math.pow(2,len(n2)-1-j)*int(n2[j])
    print(int(x*y))
