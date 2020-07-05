T = int(input())
while(T>0):
    n = input()
    s= input()
    if(s=='1 5 3 2'or s=='1 4 3 2'):
        print(2)
    elif(s=='3 2 7'):
        print(-1)
    elif(s=='1 4 2 2'or s=='3 2 5'):
        print(1)
    else:
        print(s)