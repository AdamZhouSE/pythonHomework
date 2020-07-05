#12
# 抽象处理不太好，直接对列表进行替换比较好
ori = list(input())
k = int(input())
dup = []
for item in ori:
    if item not in dup:
        dup.append(item)
cs = [0] * len(dup)
for i in range(0,len(dup)):
    for c in ori:
        if dup[i] == c:
            cs[i] += 1
small = min(cs)
i = cs.index(small)
smallOne = dup[i]
dup.remove(smallOne)
for j in range(0,len(ori)):
    if ori[j] == smallOne:
        ori[j] = dup[0]
        k -= 1
    if k == 0:
        break
count = 0
bigOne = dup[0]
for j in range(0,len(ori)):
    if ori[j] == bigOne:
        count += 1
    else:
        break
# outcome = len(ori)+k-min(cs)
print(count)

