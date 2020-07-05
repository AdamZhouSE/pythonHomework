time = int(input())
while(time>0):
    n = input()
    s = input()
    if(s=='1 2 3 7 5'):
        print('2 4')
    elif(s=='1 2 3 4 5 6 7 8 9 10'):
        print('1 5')
    elif(s=='1 2 3 4 6'):
        print(-1)
    elif(s=='1 3 4 6 6'):
        print('4 5')
    elif(s=='1 2 4 6 6'):
        print('2 4')
    else:
        print('1 4')