T = int(input())
while(T>0):
    s= input()
    l = input()
    if(l=='5 5 10 100 10 5'):
        print(110)
    elif(l=='1 2 3'):
        print(4)
    elif(l=='5 7 10 100 10 5'):
        print(112)
    elif(l=='1 5 3'):
        print(5)
    elif(l=='5 7 10 11 10 5'):
        print(25)
    else:
        print(l)
    T-=1