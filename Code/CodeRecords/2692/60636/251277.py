weights=eval(input())
d=int(input())
i=max(weights)
print(weights)
while(True):
    sum=0
    time=0
    for j in range(len(weights)):
        print(sum)
        print(time)
        if(sum+weights[j]<=i):
            sum=sum+weights[j]
        else:
            time=time+1
            sum=weights[j]
    if(sum!=0):
        time=time+1
    if(time==d):
        print(i)
        break
    else:
        i=i+1