num=int(input())
if(num<=3):
    print(num-1)
else:
    temp=1
    while(num>4):
        num-=3
        temp*=3
    print(temp*num)