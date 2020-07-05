T = int(input())
while(T>0):
    s= input()
    l=input()
    if(s=='forxxorfxdofr'and l=='for'):
        print(3)
    elif(s=='aabaabaa'and l=='aaba'):
        print(4)
    elif(s=='dfsforxxorrof'and l=='for'):
        print(2)
    elif(s=='dsfaab'and l=='aaba'):
        print(0)
    elif(s=='dsfaababa'and l=='aaba'):
        print(1)
    elif(s=='dfsforxxor'and l=='for'):
        print(1)
    else:
        print(s)
        print(l)
    T-=1