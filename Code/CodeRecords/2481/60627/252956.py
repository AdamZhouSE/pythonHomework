# 5
n = int(input())
for i in range(n):
    input()
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    t=0
    for i in a:
        if i in b:
            t+=1
    print(t)
    print(a,b)