"""
贪心算法
如果一个人的编号是x，那么他的情侣编号是x^1
对于每个x = row[i], 找到他的同伴的位置，与row[i+1]交换
"""
row = eval(input())
ans = 0
for i in range(0, len(row), 2):
    x = row[i]
    if row[i+1] == x ^ 1:
        continue
    ans += 1
    for j in range(i+1, len(row)):
        if row[j] == x ^ 1:
            row[i+1], row[j] = row[j], row[i+1]
            break
print(ans)
