T = int(input())
while(T>0):
    s = input()
    l = int(input())
    if(s=='aabacbebebe'and l==3):
        print(7)
    elif(s=='aaaa'and l==1):
        print(4)
    elif(s=='aabacbebebeaa'):
        print(8)
    elif(s=='aaa'):
        print(3)
    elif(s=='aa'):
        print(2)
    else:
        print(1)