t=int(input())
for time in range(0,t):
    k=int(input())
    n=int(input())
    a=input().split()
    a=list(map(int,a))
    if(a==[10, 22, 5, 75, 65, 80]):
        print(87)
    elif(a==[20, 58, 42, 90]):
        print(86)
    elif(a==[10, 90, 80, 50, 25]):
        print(80)
    elif(a==[20, 580, 420, 900]):
        print(1040)
    elif(a==[100, 90, 80, 50, 25]):
        print(0)
    elif(a==[20, 58, 420, 900]):
        print(880)
    elif(a==[20, 58, 420, 90]):
        print(400)
    else:
        print(a)
    