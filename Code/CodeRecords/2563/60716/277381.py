num = int(eval(input()))
if num%2==0:
    print(num-1)
else:
    ans = 3
    check = False
    while True:
        index = 1
        while True:
            temp = (1-ans**index)//(1-ans)
            if temp > num: break
            elif temp == num: 
                check = True
                break
            else:
                index+=1
        if check or ans == int(pow(num,0.5)):break
        else:
            ans+=1
    if check:
        print(ans)
    else:
        print(num-1)
