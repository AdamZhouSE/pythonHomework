import math
t=int(input())
for i in range(t):
    li=input().split()
    i=int(li[0])
    l=int(li[1])
    print(int(math.pow(2,l))-i)
    