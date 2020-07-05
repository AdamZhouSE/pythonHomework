T=int(input())
for t in range(T):
    n=int(input())
    x=int(n/9)
    y=n%9
    if y!=0:
        print(y,end='')
    print('9'*x,end='')
    print('0'*n)