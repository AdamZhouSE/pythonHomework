import math

def Sum(list1,n):
    sum=0
    for i in range(0,len(list1)):
        sum=sum+math.ceil(list1[i]/n)
    return sum

list1=list(map(int,input().split(",")))
n=int(input())
i=1
sum=Sum(list1,1)
while sum>n:
    i=i+1
    sum=Sum(list1,i)
print(i)