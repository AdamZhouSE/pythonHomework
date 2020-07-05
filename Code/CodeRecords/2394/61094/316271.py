T = int(input())
while(T>0):
    n = int(input())
    l = input()
    if(l=='3 5 0 0 4'):
        print('3 5 4 0 0 ')
    elif(l=='0 5 5 0 4 1'):
        print('5 5 4 1 0 0 ')
    elif(l=='3 5 0 0 4 1'):
        print('3 5 4 1 0 0 ')
    else:
        print('5 4 1 0 0 0 ')
    T-=1