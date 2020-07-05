num=int(input())
count=0
ans=1
nans=1
for i in range(3,num+1):
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
ncount=num-count-1 #质数

for i in range(1,count+2):
    ans*=i
for i in range(1,ncount+1):
    nans*=i
    
print((ans*nans)%(10**9+7))