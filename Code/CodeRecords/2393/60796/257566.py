import math

n=int(input())
result=[]
while n>0:
    nums=input().split(" ")
    M=int(nums[0])
    N=int(nums[1])
    ls1=input().split(" ")
    ls1=[int(x) for x in ls1]
    ls2=input().split(" ")
    ls2=[int(x) for x in ls2]
    this=0
    for i in range(M):
        for j in range(N):
            x=ls1[i]
            y=ls2[j]
            #x^y>y^x即ylnx>xlny
            if y*math.log(x)>x*math.log(y):
                this=this+1
    result.append(this)
    n=n-1

for i in range(len(result)):
    print(result[i])

