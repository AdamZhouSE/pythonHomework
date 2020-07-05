weights=eval(input())
d=int(input())
i=max(weigths)
while(True):
    sum=0
    time=0
    for j in range(len(weigths)):
        if(sum+weigths<i):
            sum=sum+weigths[j]
        else:
            time=time+1
            sum=0
    if(time==d):
        print(i)
        break