num=int(input())
while(True):
    if num%4==0:
        num=num/4
    else:
        if num==1:
            print("true")
            break
        else:
            print("false")
            break