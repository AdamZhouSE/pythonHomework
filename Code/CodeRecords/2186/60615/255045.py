count=int(input())
list=[]
while count>0:  #count sub
    sum=0

    n=int(input())
    for i in range(1,n+1):
        presum = 0
        for i in range(1,i+1):
            presum=presum+i
        sum=sum+presum
    list.append(sum)
    count=count-1
for i in list:
    print(i)