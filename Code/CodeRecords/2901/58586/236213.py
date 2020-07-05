num=int(input())
if num==1 or num==2:
    print(False)
else:
    temp=num%2
    num=num//2
    while num>0:
        if num%2==temp:
            break
        else:
            temp=num%2
            num=num//2
            
    if num==0:
        print(True)
    else:
        print(False)