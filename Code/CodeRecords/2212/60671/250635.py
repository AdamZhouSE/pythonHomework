time=int(input())
while(time>0):
    time-=1
    sum=0
    num=int(input())
    for i in range(1,num+1):
        if(num%i==0):
            sum+=i
    if(sum<2*num):
        print(1)
    else:
        print(0)