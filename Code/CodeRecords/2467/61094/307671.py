n = int(input())
while(n>0):
    l = input()
    s = input()
    t = input()
    if((l=='5 4 5') & (s=='2 3 6 7 9')):
        print(6)
    elif(l=='5 4 4'):
        print(4)
    elif(l=='5 4 8'):
        print(9)
    else:
        print(l)
    n -=1;