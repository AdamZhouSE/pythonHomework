target=int(input())
sum=0
i=0
while sum<target:
    i+=1
    sum+=i
if (sum-target)%2==0:
    print(i)
else:
    if(sum+i+1-target)%2==0:
        print(i+1)
    else:print(i+2)