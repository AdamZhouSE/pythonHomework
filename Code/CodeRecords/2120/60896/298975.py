num=eval(input())
result=1
if(num<4):
    if(num==2):
        print(1)
    if(num==3):
        print(2)
else:
    while(num>4):
        num-=3
        result*=3
    result*=num
    print(result)

