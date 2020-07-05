def confirm_corner(a, n):
    res = False
    count_1 = 0
    if a[0][1] == 'o':
        count_1 += 1
    if a[1][0] == 'o':
        count_1 += 1
    count_2 = 0
    if a[0][n - 2] == 'o':
        count_2 += 1
    if a[1][n - 1] == 'o':
        count_2 += 1
    count_3 = 0
    if a[n - 2][0] == 'o':
        count_3 += 1
    if a[n - 1][1] == 'o':
        count_3 += 1
    count_4 = 0
    if a[n - 1][n - 2] == 'o':
        count_4 += 1
    if a[n - 2][n - 1] == 'o':
        count_4 += 1
    if count_1 % 2 == 0 and count_2 % 2 == 0 and count_3 % 2 == 0 and count_4 % 2 == 0:
        res = True
    return res


def confirm_edge(a, n):
    res = True
    for i in range(1, n - 1):
        count_1 = 0
        if a[0][i - 1] == 'o':
            count_1 += 1
        if a[0][i + 1] == 'o':
            count_1 += 1
        if a[1][i] == 'o':
            count_1 += 1
        count_2 = 0
        if a[i - 1][0] == 'o':
            count_2 += 1
        if a[i + 1][0] == 'o':
            count_2 += 1
        if a[i][1] == 'o':
            count_2 += 1
        count_3 = 0
        if a[i - 1][n - 1] == 'o':
            count_3 += 1
        if a[i + 1][n - 1] == 'o':
            count_3 += 1
        if a[i][n - 2] == 'o':
            count_3 += 1
        count_4 = 0
        if a[n - 1][i - 1] == 'o':
            count_4 += 1
        if a[n - 1][i + 1] == 'o':
            count_4 += 1
        if a[n - 2][i] == 'o':
            count_4 += 1
        if count_1 % 2 == 1 or count_2 % 2 == 1 or count_3 % 2 == 1 or count_4 % 2 == 1:
            res = False
            break
    return res


n = int(input())
a = []
for i in range(n):
    a.append([i for i in input()])
if n == 1:
    print("YES")
elif n == 2:
    if a[0][0] == a[1][1] and a[0][1] == a[1][0]:
        print("YES")
    else:
        print("NO")
else:
    if confirm_corner(a, n) and confirm_edge(a, n):
        res = "YES"
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                count = 0
                if a[i - 1][j] == 'o':
                    count += 1
                if a[i + 1][j] == 'o':
                    count += 1
                if a[i][j - 1] == 'o':
                    count += 1
                if a[i][j + 1] == 'o':
                    count += 1
                if count % 2 == 1:
                    res = "NO"
                    break
        print(res)
    else:
        print("NO")
