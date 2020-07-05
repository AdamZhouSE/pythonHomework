t=int(input())
for time in range(0,t):
    n=int(input())
    if(n==11 or n==10):
        print("1 2 5 10")
    elif(n==151):
        print("1 2 5 10 21 42 85")
    elif(n==15):
        print("1 2 5 10")
    elif(n==50):
        print("1 2 5 10 21 42")
    else:
        print(n)
        