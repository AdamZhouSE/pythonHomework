n, m = map(int, (input().strip().split(" ")))
temp = [None]*n
ans = []
cnt = 1
for j in range(n):
    temp[j] = []
for i in range(m):
    c, a, b = map(int, (input().strip().split(" ")))
    if c == 1:
        for k in range(a - 1, b):
            if temp[k] == []:
                temp[k] = [cnt]
            else:
                temp[k] = temp[k]+[cnt]         # 二维数组赋值的敏感点
        cnt += 1
    else:
        ans = temp[a]
        for k in range(a-1, b):
            for l in temp[k]:
                if l not in ans:
                    ans.append(l)
        print(len(ans))
        ans = []
