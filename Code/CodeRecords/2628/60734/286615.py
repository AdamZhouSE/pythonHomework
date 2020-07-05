def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)

t = int(input())
points = []
for i in range(t):
    lst = list(map(int,input().split(' ')))
    a, b = lst[0], lst[1]
    lst = list(map(int,input().split(' ')))
    c, d = lst[0], lst[1]
    lst = list(map(int,input().split(' ')))
    e, f = lst[0], lst[1]

    s = abs((a*d+c*f+b*e-a*f-b*c-d*e)/2)
    l1 = gcd(abs(a - c), abs(b - d))
    l2 = gcd(abs(a - e), abs(b - f))
    l3 = gcd(abs(c - e), abs(d - f))
    print(int(s-(l1+l2+l3)/2+1))