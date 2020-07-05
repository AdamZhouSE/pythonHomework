# 5
k = int(input())

def f(n):
    n2 = 0
    n5 = 0
    for i in range(1,n+1):
        a = i
        b = i
        while(a%2 == 0):
            a = int(a /2)
            n2 += 1
        while(b%5 == 0):
            b =int(b /5)
            n5 += 1
    return min([n2,n5])
n = 0
for i in range(1000):
    if f(i) == k:
        n += 1
print(n)