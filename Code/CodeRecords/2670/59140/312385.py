import math
t=int(input())
for _ in range(t):
    temp=int(input())
    print(pow(2,int(math.log(temp,2))+1)-temp-1)