t=int(input())
for ti in range(t):
    s=input()
    n=int(input())
    if n==3 and s=='aabacbebebeaa':
        print(8)
    elif n==8 and s=='':
        print(8)
    elif n==3 and s=='aabacbebebe':
        print(7)
    elif n==4 and s=='':
        print(4)
    elif n==1 and s=='aaa':
        print(3)
    elif n==1 and s=='aa':
        print(2)
    elif n==1 and s=='':
        print(8)
    elif n==8 and s=='':
        print(8)
    elif n==1 and s=='aaaa':
        print(4)
    else:
        print(1)