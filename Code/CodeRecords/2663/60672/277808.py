def regular(n):
    a=3+7*n-7+(n-1)*(n-2)*2
    return a

T=int(input())
for i in range(T):
    k=int(input())
    print(regular(k))