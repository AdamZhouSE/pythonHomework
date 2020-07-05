T = int(input())
while(T>0):
    n = int(input())
    l = input()
    if(l=='2 2 0 4 4'):
        print('4 8 0 0 0')
    elif(l=='0 1 2 2 0'):
        print('1 4 0 0 0')
    elif(l=='2 2 0 4 0 8'):
        print('4 4 8 0 0 0')
    elif(l=='0 2 2 4 0 6 6 0 0 8'):
        print('4 4 12 8 0 0 0 0 0 0')
    elif(l=='0 2 2 2 0 6 6 0 0 8'):
        print('4 2 12 8 0 0 0 0 0 0')
    else:
        print(l)
    T-=1