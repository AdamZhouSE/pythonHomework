num=int(input())
if num<=3:
    print(num-1)
else:
    if num%3==0:
        print(pow(3,num//3))
    elif num%3==1:
        print(pow(3,num//3-1)*4)
    else:
        print(pow(3,num//3)*2)