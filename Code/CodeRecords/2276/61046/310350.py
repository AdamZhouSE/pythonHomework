R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
out = [[r0, c0]]
for i in range(1, (max([r0, c0, R-r0-1, C-c0-1])+1)*2):  # 缩小搜索空间
    add = i % 2 == 1  # 加减状态
    for j in range(i):
        c0 += 1 if add else -1
        if (add and c0 >= C) or (not add and c0 < 0):  # 越界后跳过后续累加
            c0 += i - j - 1 if add else -(i - j - 1)
            break
        if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C: out.append([r0, c0])  # 符合条件判断
    for j in range(i):
        r0 += 1 if add else -1
        if (add and r0 >= R) or (not add and r0 < 0):
            r0 += i - j - 1 if add else -(i - j - 1)
            break
        if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C: out.append([r0, c0])
print(out)