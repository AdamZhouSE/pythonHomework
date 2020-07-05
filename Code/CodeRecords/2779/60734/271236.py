def gcd(a,b):
    while b!=0:
        temp = a%b
        a = b
        b = temp
    return a

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    a = max(lst)
    b = min(lst)
    print(a*b//gcd(a,b))