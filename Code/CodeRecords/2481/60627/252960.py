# 5
n = int(input())
for i in range(n):
    input()
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    a = set(a)
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    b = set(b)
    t=0
    for i in a:
        if i in b:
            t+=1
    print(t)