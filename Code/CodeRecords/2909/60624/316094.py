from collections import Counter
def func18():
    s = input().strip()
    maxLetters = int(input())
    minSize = int(input())
    maxSize = int(input())
    res = []
    # 先把符合条件的全部搜集起来
    for i in range(0, len(s) - minSize + 1):
        ts = s[i:i + minSize]
        if len(set(ts)) > maxLetters:
            continue
        else:
            res.append(ts)
    if not res:
        print(0)
        return 
    # 返回出现次数最多的
    print(sorted(Counter(res).items(), key=lambda x: x[1], reverse=True)[0][1])
    return
func18()