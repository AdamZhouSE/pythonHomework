num=int(input())
nums=list(map(int,input().split(" ")))
count=0
countp=0
countn=0
counto=0
for i in nums:
    if i>1:
        count+=i-1
        countp+=1
    elif i<-1:
        count+=-1-i
        countn+=1
    elif i==0:
        count+=1
        counto+=1
    elif i==-1:
        countn+=1
if counto==0 and countn%2==1:
    count+=2
print(count)