a=eval(input())
for i in range(a):
    x1=2
    x2=1
    temp=0
    b=eval(input())
    if(b==0):print(x1)
    elif(b==1):print(x2)
    else:
        for i in range(b-1):
            temp=x2
            x2+=x1
            x1=temp
        print(x2)
            