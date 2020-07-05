T = int(input())
for _ in range(T):
    a = [int(x) for x in input().split(' ')]
    n = a[0]
    x = a[1]
    ar = (n-1)*x
    doc = (n-1)*10
    if x > 10:
        print(0)
    else:
        print(doc-ar)

