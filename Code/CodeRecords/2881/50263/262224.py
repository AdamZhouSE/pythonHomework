n = int(input())
for i in range(n):
    for j in range(n):
        if j < abs((n+1)/2-i-1) or j>n-1-abs((n+1)/2-i-1):
            print('*',end='')
        else:
            print('D',end='')
        if j == n-1:
            print('')
        