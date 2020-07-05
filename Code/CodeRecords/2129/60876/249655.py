num=int(input())
time=0
while num!=1:
    if num%2==0:
        num=num//2
    elif num==3:
        time+=2
        break
    else:
        if (num+1)%4==0:
            num+=1
        else:
            num-=1
    time+=1
print(time)