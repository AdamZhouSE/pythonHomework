time=int(input())
while(time>0):
    time-=1
    num=int(input())
    sum=0
    for i in range(1,num+1):
        temp=0
        for j in range(1,i+1):
            temp+=(2*j-1)
        sum+=temp
    print(sum)