'''
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''

from collections import Counter

inp = input()
barcodes = inp[1:len(inp)-1].split(",")
data = []
for i,j in Counter(barcodes).most_common():
    data += [i] * j
l = len(data)
res = [0] * l
res[::2] = data[:(l+1)//2]
res[1::2] = data[(l+1)//2:]
res = list(map(int, res))
print(res)