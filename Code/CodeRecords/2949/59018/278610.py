inp=input()
if inp=='1 0':
    print('1')
    print( )
    
else:
    info=inp[0:-2].split(' ')
    info.reverse()
    print(int(''.join(info)))


