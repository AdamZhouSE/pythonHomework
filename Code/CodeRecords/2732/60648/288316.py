def modmod(m,n,p):
    if n==0:
        return 1
    if n%2==0:
        w=modmod(m,n//2,p)
        return (w*w)%p


if __name__=="__main__":
    n=int(input())
    for i in range(n):
        m,n,p=map(int,input().split(' '))
        x=modmod(m,n,p)
        print(x)