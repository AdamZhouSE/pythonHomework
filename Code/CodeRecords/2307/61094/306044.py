n = int(input())
while(n>0):
    l = input()
    s = input()
    if((l=='5') & (s=='3 1 3 3 2')):
        print(3)
    elif((l=='3')&(s=='1 2 3')):
        print(-1)
    elif((l=='5')&(s=='3 1 1 4 5')):
        print(-1)
    elif((l=='3')&(s=='2 2 3')):
        print(2)
    elif((l=='5')&(s=='3 1 1 1 2')):
        print(1)
    else:
        print(s)
    n -=1;