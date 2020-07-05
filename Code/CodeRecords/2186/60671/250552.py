time=int(input())
while(time>0):
    num=int(input())
    sum=0
    for i in range(2,num+1):
        temp=0
        for j in range(1,i+1):
            temp+=j
        sum+=temp
    sum+=1
    print(sum)