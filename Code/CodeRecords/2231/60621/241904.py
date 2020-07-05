a=eval(input())
for i in range(a):
    b=eval(input())
    v=2
    count=0
    while v<=b:
        if(b%v==0):
            count+=1
            b/=v
        else:
            v+=1
    if(count==3):
        print("1")
    else:
        print("0")