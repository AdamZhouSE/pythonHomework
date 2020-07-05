a=int(input())
if a<0:
    print('-',end='')
    b=list(str(a))
    b.pop(0)
    b.reverse()
    while b[0]=='0':        
        b.pop(0)
    print(''.join(b))

else:
    b=list(str(a))
    b.reverse()
    while b[0]=='0':
        
        b.pop(0)
    print(''.join(b))
