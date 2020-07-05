n=int(input())
for i in range(n):
    N=int(input())
    x=N%9
    y=int(N/9)
    if y==0:
        print(str(x)+"0"*N)
    else:
        print(str(x)+"9"*y+"0"*N)