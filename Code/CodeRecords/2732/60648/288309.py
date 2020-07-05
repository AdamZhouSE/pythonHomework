def modmod(m,n,p):
    if m


if __name__=="__main__":
    n=int(input())
    for i in range(n):
        m,n,p=map(int,input().split(' '))
        x=modmod(m,n,p)
        print(x)