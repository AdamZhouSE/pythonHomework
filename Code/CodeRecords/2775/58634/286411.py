t = int(input())
for i in range(t):
    n = int(input())
    if n%3 == 0:
        print(n//3-1,n//3,n//3+1)
    else:
        print(-1)