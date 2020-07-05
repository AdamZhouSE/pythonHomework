def add(n):
    sum=0
    for i in range(n):
        sum=sum+i+1
    return sum
num=int(input())
for k in range(num):
    n=int(input())
    res=[]
    for i in range(n):
        res.append(0)
    time=1
    step=0
    while(time<=n):
        for i in range(n):
            if res[i]==0:
                step=step+1
                if step==add(time)+time:
                    res[i]=time
                    time=time+1
            else:
                pass
    for i in range(len(res)):
        if i!=len(res)-1:
            print(res[i],end=" ")
        else:
            print(res[i])
    

