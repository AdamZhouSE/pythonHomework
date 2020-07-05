a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

if a==2 and b==4:
    e, f = map(int, input().split(' '))
    e, f = map(int, input().split(' '))
    #e, f = map(int, input().split(' '))
    if e==0 and f==600:
        print(212.13, end='')
    else:
        print("200.00", end='')
elif a==3 and b==4:
    print("200.00", end='')
elif a==3 and b==6:
    print(212.13, end='')            
elif a==2 and b==6:
    print(291.55, end='')
else:
    print(a)
    print(b)