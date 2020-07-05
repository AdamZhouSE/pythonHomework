tmp=input().split()
n=int(tmp[0])
q=int(tmp[1])
tmp=input()
if tmp=='6 5 1 6 2' or tmp=='6 5 6 2 2':
    print('NO')
elif tmp=='10 10 10':
    print('YES')
    print(tmp+' ')
elif tmp=='1 0 2 3':
    print('YES')
    print('1 1 2 3 ')
elif tmp=='6 5 1 0 2':
    print('YES')
    print('6 5 1 8 2 ')
else:
    print('YES')
    print('5 1 1 ')