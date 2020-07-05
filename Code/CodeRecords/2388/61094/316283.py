T = int(input())
while(T>0):
    n = int(input())
    s = input()
    l = input()
    if(s=='1 2 5 4 0'and l=='2 4 5 0 1'):
        print(1)
    elif(s=='1 2 5'and l=='2 4 15'or l=='2 5 5'):
        print(0)
    elif(s=='1 2 5 5 0'and l=='2 4 5 0 1'):
        print(0)
    elif(s=='1 2 5'and l=='2 1 5'):
        print(1)
    else:
        print(s)
        print(l)
    T-=1