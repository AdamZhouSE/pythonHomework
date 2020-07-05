def st(a):
    if a==1:
        return '1 '
    else:
        return st(a-1)+str(a)+' '
t=int(input())
for i in range(t):
    n=int(input())
    s=st(n)
    print(s)
    