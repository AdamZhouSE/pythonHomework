n=int(input())
sum=1
for i in range(1,n+1):
    sum*=i
count=0
while(sum%10==0):
    count+=1
    sum=sum/10
print(count)