a=eval(input())
i=0
while i<a:
    b=eval(input())
    i2=1
    num=0
    while i2<=b:
        num=num+i2**5
        i2=i2+1
    i=i+1
    print(num)