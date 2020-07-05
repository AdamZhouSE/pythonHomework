def solve():
    n=int(input())
    for i in range(int(n/2)):
        for j in range(int((n-2*i-1)/2)):
            print('*',end='')
        for j in range(2*i+1):
            print('D',end='')
        for j in range(int((n-2*i-1)/2)):
            print('*',end='')
        print('')
    for i in range(n):
        print('D', end='')
    print('')
    for i in range(int(n/2)):
        for j in range(i+1):
            print('*',end='')
        for j in range(n-2*i-2):
            print('D',end='')
        for j in range(i+1):
            print('*',end='')
        print('')

if  __name__ == '__main__' :
    solve()