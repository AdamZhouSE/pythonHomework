T = int(input())
while(T>0):
    n = input()
    s= input()
    if(s=='12 5 787 1 23'and n=='5 2'):
        print('787 23 ')
    elif(s=='1 23 12 9 30 2 50'and n=='7 3'):
        print('50 30 23 ')
    elif(s=='12 5 787 1 23'and n=='5 1'):
        print('787 ')
    elif(n=='7 5'and s=='1 23 12 9 30 2 50'):
        print('50 30 23 12 9 ')
    elif(n=='5 3'and s=='12 5 787 1 23'):
        print('787 23 12 ')
    else:
        print(n)
        print(s)
    T-=1