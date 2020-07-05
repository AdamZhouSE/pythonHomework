a=int(input())
if a<0:
    print('-',end='')
    b=list(str(a))
    b.pop(0)
    b.reverse()
    print(''.join(b))

else:
    b=list(str(a))
    b.reverse()
    print(''.join(b))
