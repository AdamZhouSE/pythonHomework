import collections
import sys

def smallestStringWithSwaps(s,pairs):
    p = {i: i for i in range(len(s))}  # 初始化并查集

    def f(x):
        if x != p[x]:
            p[x] = f(p[x])
        return p[x]

    for i, j in pairs:
        p[f(j)] = f(i)
        # 合并可交换位置
    d = collections.defaultdict(list)
    for i, j in enumerate(map(f, p)):
        d[j].append(i)
    # 排序
    ans = list(s)
    for q in d.values():
        t = sorted(ans[i] for i in q)
        for i, c in zip(sorted(q), t):
            ans[i] = c
    return ''.join(ans)

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

s = Input[0]
li = list(Input[1])
arr = []
for item in li:
    if item.isdigit():
        arr.append(int(item))
pairs = []
for i in range(0,len(arr),2):
    pairs.append([arr[i],arr[i+1]])

print(smallestStringWithSwaps(s,pairs),end="")