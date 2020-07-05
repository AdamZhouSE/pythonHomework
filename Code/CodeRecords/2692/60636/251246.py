weights=eval(input())
d=int(input())
i=max(weights)
while(True):
    sum=0
    time=0
    for j in range(len(weights)):
        if(sum+weights[j]<i):
            sum=sum+weights[j]
        else:
            time=time+1
            sum=0
    if(time==d):
        print(i)
        break