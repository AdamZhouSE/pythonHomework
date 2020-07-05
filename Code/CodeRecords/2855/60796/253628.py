n = int(input())
ls = []
for i in range(n):
    m = input()
    l = []
    for j in range(n):
        l.append(m[j])
    ls.append(l)
result = ""
r = 0
for i in range(n):
    for j in range(n):  # 现在是ls[i][j]
        total = 0
        if i > 0:  # 有上
            if ls[i - 1][j] == 'o':
                total = total + 1
        if i < n - 1:  # 有下
            if ls[i + 1][j] == 'o':
                total = total + 1
        if j < n - 1:  # 有右
            if ls[i][j + 1] == 'o':
                total = total + 1
        if j > 0:  # 有左
            if ls[i][j - 1] == 'o':
                total = total + 1
        if total % 2 == 0 or total==0:
            r=r+1
      #  print(total)

if r==n*n:
    print("YES")
else:
    print("NO")


        