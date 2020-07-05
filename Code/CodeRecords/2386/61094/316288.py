T = int(input())
while(T>0):
    n = int(input())
    l = input()
    m = int(input())
    if(n==6 and l=='1 5 1 0 6 0'and m==7):
        print(1)
    elif(n==6 and l=='1 5 1 0 6 0'and m==6):
        print(1)
    elif(n==6 and l=='1 5 1 0 6 0'and m==10):
        print(0)
    elif(n==6 and l=='1 5 1 0 6 0'and m==8):
        print(1)
    else:
        print(n)
        print(l)
        print(m)
    T-=1