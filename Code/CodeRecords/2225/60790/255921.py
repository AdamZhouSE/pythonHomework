def func(m,n):
    if n==0:
        return 0
    if m==0:
        return 1
    if n==1:
        return 2
    if n==2:
        return 3 if m==1 else 4
    if m==1:
        return 4
    if m==2:
        return 7
    return 8
n=int(input())
m=int(input())
print(func(m,n))