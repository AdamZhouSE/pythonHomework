# 贪心算法
# 将字母按照出现次数从大到小排序。
# 每次优先选择剩余次数最多，且与新字符串末尾字符串不重复的字符，排在末尾。
# 若某次选择无法找出这样的字符，则返回空串。
from collections import Counter
S = input()
cnt = Counter(S)
res = "#"
while cnt:
    stop = True
    for v, _ in cnt.most_common():
        if v != res[-1]:
            stop = False
            res += v
            cnt[v] -= 1
            if cnt[v] == 0:
                del cnt[v]
            break
    if stop:
        break
res = res[1:] if len(res) == len(S)+1 else ""
print(res)
