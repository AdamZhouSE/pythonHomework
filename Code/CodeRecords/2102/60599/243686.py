n=int(input())
sum=0
for i in range(2,n):
    flag=0
    for z in range(2,i//2+1):
        if i%z==0:
            flag=1
            break
    if(flag==0):
        sum+=1
print(sum)