t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    t = [int(i) for i in input().split()]
    t.sort(reverse=True)
    a = 0
    b = 0
    for k in t:
        if a <= b:
            a += k
        else:
            b += k
    ans_l.append(abs(a - b))
for i in ans_l:
    print(i)
