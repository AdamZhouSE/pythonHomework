t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    sum = 0
    bas = a[0]
    cnt = 1
    for j in range(1, len(a)):
        if a[j] == bas:
            cnt += 1
        else:
            sum += (cnt // 2) * 2
            cnt = 1
            bas = a[j]
    sum += (cnt // 2) * 2
    ans_l.append(sum)
for i in ans_l:
    print(i)