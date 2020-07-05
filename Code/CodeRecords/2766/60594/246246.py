n=(int)(input())
for index in range(n):
    n=(int)(input())
    if (n-1)%5==0:
        print(1)
    elif (n-2)%5==0:
        print(2)
    elif(n-3)%5==0:
        print(3)
    elif (n-4)%5==0:
        print(4)
    else:
        print(-1)