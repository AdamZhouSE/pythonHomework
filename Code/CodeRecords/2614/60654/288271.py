a = int(input())
for i in range(a):
    a1 = int(input())
    b = list(map(int,input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    for j in range(a1):
        if b[j]-c[j] in d:
            print(d.index(b[j]-c[j]))