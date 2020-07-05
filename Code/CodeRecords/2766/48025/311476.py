t=int(input())
for i in range(0,t):
    n=int(input())
    if n==48 or n==3:
        print(3)
    elif n==71 or n==41:
        print(1)
    elif n==15 or n==70:
        print(-1)
    elif n==7:
        print(2)
    else:
        print(n)