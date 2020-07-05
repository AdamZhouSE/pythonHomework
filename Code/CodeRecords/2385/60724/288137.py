def num(n):
    if n==1:
        return 2
    elif n==2:
        return 3
    else:
        return num(n-2)+num(n-1)
def re(n):
    if n==2:
        return 3
    else:
        return re(n-1)+num(n-2)

T=int(input())
for i in range(T):
    N=int(input())
    print(re(N))