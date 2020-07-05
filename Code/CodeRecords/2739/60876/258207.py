k,n=map(int,input().split(","))
def f(k,n,start):
    if k==1 and start<=n:
        return[[n]]
    else:
        return[[]]
print(f(k,n,1))