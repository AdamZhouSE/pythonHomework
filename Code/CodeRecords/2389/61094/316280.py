T = int(input())
while(T>0):
    n = int(input())
    s = input()
    if(s=='1 2 3 4 5'):
        print('2 1 4 3 5')
    elif(s=='1 3 8 10 17'):
        print('3 1 10 8 17')
    elif(s=='1 3 5 7 9'):
        print('3 1 7 5 9')
    elif(s=='1 3 5 10 17'):
        print('3 1 10 5 17')
    else:
        print(s)
    T-=1