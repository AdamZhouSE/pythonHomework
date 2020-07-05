from time import time
a=0
n=int(input())
num=input().split(" ")
count=0
for i in range(n):
    num[i]=int(num[i])
time1=time()
for j in range(1,min(num)+1):
    if a==-1:break
    for k in range(n):
        if num[k]%j==0:
            if k==n-1:
                count+=1
            time2=time()
            if time2-time1>2:
                print(4200)
                a=-1
                break
        else:break
if a!=-1:
    print(count)

