n=int(input())
for i in range(int(n/2)+1):
    for j in range(int(n/2)-i):
        print('*',end='')
    for j in range(2*i+1):
        print('D',end='')
    for j in range(int(n/2)-i):
        print('*',end='')
    print()
for i in range(int(n/2)-1,-1,-1):
    for j in range(int(n/2)-i):
        print('*',end='')
    for j in range(2*i+1):
        print('D',end='')
    for j in range(int(n/2)-i):
        print('*',end='')
    print()