n=int(input())
count=0
for x in range(1,n+1):
    if(x%10==1):
        count+=1
    if(x//10==1):
        count+=1
    if(x//100==1):
        count+=1
print(count)