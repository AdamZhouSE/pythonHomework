def find(n):
    if n==1:
        return 1
    elif n==0:
        return 2
    else:
        return find(n-1)+find(n-2)
N=int(input())
for i in range(0,N):
    n=int(input())
    print(find(n)%1000000007)