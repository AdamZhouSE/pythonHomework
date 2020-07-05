a=eval(input())
for i in range(a):
    b=eval(input())
    v=2
    count=0
    flag=1
    while v<=b:
        if(b%v==0 ):
            if(flag==1):
                flag=0
                count+=1
                b/=v
            else:
                count=0
                break
        else:
            flag=1
            v+=1
    if(count==3):
        print("1")
    else:
        print("0")