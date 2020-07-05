n=int(input())
a=int(input())
b=int(input())
count=0
i=1
while(count<n):
    if(i%a==0 or i%b==0):
        count+=1
    i+=1
i=i-1
print(i%(10**9+7))