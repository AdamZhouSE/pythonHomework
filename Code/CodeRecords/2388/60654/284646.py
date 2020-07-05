a = int(input())
for i in range(a):
    sign = 1
    b = int(input())
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    for j in c:
        if j in d:
            d.remove(j)
        else:
            sign = 0
            break
    if not c:
        sign = 1
    print(sign)