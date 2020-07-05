T = int(input())
for ttt in range(T):
    n = int(input()) - 1
    print(int(n*(n+1)*(2*n+1)/12+3*n*(n+1)/4+n)+1)