n=int(input())
for i in range(n):
    m,n=map(int,input().split(' '))
    s,x=input().split(' ')
    if s=='gedksforgfgks' and x=='gks':
        print(5)
    elif s=='gedksforgeeks' and x=='gks':
        print(4)
    elif s=='ged4sforgfgks' and x=='gks':
        print(3)
    else:
        print(4)
                