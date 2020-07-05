import math
num=int(input())
sticks=list(map(int,input().split()))
result=[]
for i in range(num//2):
    a=sum(sticks[i:i+num//2])
    b=sum(sticks)-a
    result.append(math.sqrt(a)+math.sqrt(b))
print(max(result))