time=int(input())
while(time>0):
    time-=1
    num=int(input())
    temp=1
    for i in range(1,num+1):
        temp+=2*i-1
    print(num*temp)