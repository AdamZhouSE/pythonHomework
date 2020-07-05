import math
n = int(input())
a = [int(i) for i in input().split()]
cars = 0
n1,n2,n3,n4 = 0,0,0,0
for item in a:
    if(item == 1):
        n1+=1
    elif(item == 2):
        n2+=1
    elif(item == 3):
        n3+=1
    else:
        n4+=1
cars += n4
cars += n3
if(n3>=n1):
    cars += math.ceil(n2/2)
    print(cars)
else:
    n1 -= n3
    if(n2%2 == 0):
        cars += int(n2/2)
        cars += math.ceil(n1/4)
        print(cars)
    else:
        cars += int(n2/2)+1
        if(int(n1%4) <= 2):
            cars += int(n1/4)
        else:
            cars += math.ceil(n1/4)
        print(cars)