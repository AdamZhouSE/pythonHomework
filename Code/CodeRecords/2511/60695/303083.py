ns = input().split(" ")
n = int(ns[0])
s = int(ns[1])
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    if (n - i) % 2 == 1:
        m = n - 2
    else:
        m = n - 1
    flag = True
    for j in range(m, i, -2):
        sum1, sum2 = 0, 0
        for k in range(i, (i + j + 1) // 2):
            sum1 += a[k]
        for k in range((i + j + 1) // 2, j + 1):
            sum2 += a[k]
        if sum1 <= s and sum2 <= s:
            print(j - i + 1)
            flag = False
            break
    if flag:
        print(0)
print(0)