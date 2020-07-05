def x(n):
    count=0
    while n>0:
        if n%10==1:
            count=count+1
            n=(n-1)//10
        else:
            n=(n-n%10)//10
    return count
a=int(input())
sum=0
for i in range(1,a+1):
    sum=sum+x(i)
print(sum)