n=(int)(input())
m=(int)(n/2)
for i in range(m):
    for j in range(n):
        if(j<m-i or j >m+i):
            if(j==n-1):
                print('*')
            else:
                print('*',end='')
        else:
            print('D',end='')
for i in range(m,n):
    for j in range(n):
        if(j<i-m or j>n+m-i-1):
            if (j == n - 1):
                print('*')
            else:
                print('*', end='')
        else:
            if (j == n - 1):
                print('D')
            else:
                print('D', end='')