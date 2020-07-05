def l(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    return l(n-1)+l(n-2)
n=int(input())
for i in range(n):
    a=int(input())
    print(l(a))