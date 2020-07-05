# 题目描述
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
#
# 请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#
# 1 <= barcodes.length <= 10000
#
# 1 <= barcodes[i] <= 10000

import collections

li = list(eval(input().strip()))
leng = len(li)

c = collections.Counter(li)
c = sorted(c.items(), key=lambda vi: vi[1], reverse=True)
idx = 0
iidx = 0
cidx = 0
resli = []
reslii = [-1 for j in range(leng)]

for i in c:
    for j in range(i[1]):
        resli.append(i[0])
while iidx < leng:
    reslii[iidx] = resli[idx]
    iidx += 2
    idx += 1

iidx = 1
while iidx < leng:
    reslii[iidx] = resli[idx]
    iidx += 2
    idx += 1


print(reslii)