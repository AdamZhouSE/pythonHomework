def pow(x):
    sum=1
    for i in range(0,x):
        sum=sum*3
    return sum
a=int(input())
if a==2:
    print("1")
elif a==3:
    print("2")
else:
    if a%3==0:
        b=pow(a//3)
        print(b)
    elif a%3==1:
        b=pow(a//3-1)*4
        print(b)
    else:
        b = pow(a//3) * 2
        print(b)
