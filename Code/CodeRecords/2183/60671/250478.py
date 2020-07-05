#2 6 12 20n*(n+1
time=int(input())
while(time>0):
    time-=1
    num=int(input())
    num1=(num-1)*num+1
    num2=num*(num+1)
    sum=0
    for i in range(num1,num2+1):
        sum+=i
    print(sum)