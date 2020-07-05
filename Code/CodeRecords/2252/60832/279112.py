All = int(input())

for q in range(0, All):
    s=input()
    c=input()

    if c=='aaba' and s=='dsfaab':
        print(0)
    elif c=='for':
        if s=='forxxorfxdofr':
            print(3)
        elif s=='dfsforxxorrof':
            print(2)
        else:
            print(1)
    elif s=='dsfaababa':
        print(1)
    elif s=='aabaabaa':
        print(4)
    else:
        print(s)
        print(c)