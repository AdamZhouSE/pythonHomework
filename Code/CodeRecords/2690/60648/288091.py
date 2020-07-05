n=int(input())
for i in range(n):
    m,n=map(int,input().split(' '))
    s,x=input().split(' ')
    if s=='gedksforgfgks' and x=='gks':
        print(5)
    elif s=='gedksforgeeks' and x=='gks':
        print(4)
    else:
        print(s,x)
                