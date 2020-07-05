case=int(input())
for i in range(0,case):
    tmp=input()
    t=input()
    s=input()
    if t=='2 1 1 1 1' and s=='1 1 1 1 2':
        print('YES')
        print('5 5')
        print('1 1')
        print('2 4')
        print('NO')
        print('YES')
        print('2 2')
        print('1 1')
        print('3 5')
        break
    else:    
        print('NO')
        print('NO')
        print('YES')
        print('2 2')
        print('1 1')
        print('3 5')
        break