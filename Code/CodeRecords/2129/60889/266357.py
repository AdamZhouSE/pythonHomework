num = int(input())
time = 0
while num!=1:
    if num%2==0:
        num = num/2
    else:
        if num==3:
            num = num-1
        elif (num+1)%4==0:
            num = num + 1
        else:
            num = num - 1
    time = time + 1
print(time)