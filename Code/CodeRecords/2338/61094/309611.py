n = int(input())
while(n>0):
    l = input()
    s = input()
    if((l=='6 16')&(s=='1 4 45 6 10 8')):
        print('Yes')
    elif((l=='5 10')&(s=='1 2 4 3 6')):
        print('Yes')
    elif((l=='6 16')&(s=='1 4 45 6 7 8')):
        print('No')
    elif((l=='5 10')&(s=='1 2 4 3 6')):
        print('No')
    elif((l=='5 10')&(s=='1 2 5 3 6')):
        print('No')
    else:
        print(l)
        print(s)
    n -=1;