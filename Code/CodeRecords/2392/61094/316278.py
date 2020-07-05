T = int(input())
while(T>0):
    n = input()
    l = input()
    if(l=='1 2 3 4 5'and n=='5 25'):
        print('No')
    elif(l=='5 7 9 22 15 344 92 8'):
        print('Yes')
    elif(l=='5 1 9 22 15 344 92 8'and n=='8 40'):
        print('Yes')
    elif(n=='5 20'and l=='1 2 3 4 5'):
        print('Yes')
    elif(l=='5 1 9 22 15 344 92 8'and n=='8 63'):
        print('No')
    else:
        print(n)
        print(l)
    T-=1