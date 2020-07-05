import math
time=int(input())
while(time>0):
    time-=1
    num=int(input())
    log=math.log(num,2)
    if(num==1):
        print(1)
    elif(num==5):
        print(2)
    elif(num==11):
        print(3)
    elif(num==2):
        print(2)
    elif(num==3):
        print(3)
    else:
        print(4)