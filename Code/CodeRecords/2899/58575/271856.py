num=int(input())
flag='true'
if num<0:
    print('false')
elif num==1:
    print('true')
else:
    while num>4:
        if num%10!=4 and num%10!=6:
            flag='false'
            break
        else:
            num=num//4
    if num<4:
        flag='false'
    print(flag)