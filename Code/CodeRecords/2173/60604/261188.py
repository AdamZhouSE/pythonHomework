def g(n):
    if n==801:
        return n*n+170986800
    elif n>1:
        return n*n+g(n-1)
    else:
        return 1
n=int(input())
for I in range(n):
    n=int(input())
    print(g(n))
    #print(g(800))