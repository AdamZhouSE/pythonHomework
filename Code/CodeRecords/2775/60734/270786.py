t = int(input())
for i in range(t):
    n = int(input())
    if (n//3)*3 == n:
        print('{} {} {}'.format(n//3-1,n//3,n//3+1))
    else:
        print(-1)