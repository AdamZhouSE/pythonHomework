import math

n=int(input())
x=input()
lis=list(map(int,x.split(" ")))

lis=sorted(lis)
sum=0
for i in range(0,len(lis)//2):
    sum=sum+int(math.pow(lis[i]+lis[len(lis)-1-i],2))
print(sum)