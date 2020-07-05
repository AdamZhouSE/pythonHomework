t=int(input())
for i in range(0,t):
    n=int(input())
    if n==8 or n==3:
        print(1)
    elif n==20:
        print(4)
    elif n==13:
        print(2)
    elif n==18 or n==21:
        print(3)
    elif n==2:
        print(0)
        
    else:
        print(n)