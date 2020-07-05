# 题目描述
# 给定一个由表示变量之间关系的字符串方程组成的数组，
# 每个字符串方程 equations[i] 的长度为 4，
# 并采用两种不同的形式之一："a==b" 或 "a!=b"。
# 在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
#
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。

def union(li, set1, set2):
    if set1 == set2: return
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

if __name__ == '__main__':

    inLi = list(eval(input()))
    equalSets = []

    for i in inLi:
        if i[1] == "=":
            op1 = i[0]
            op2 = i[3]
            s1 = None
            s2 = None
            for idx in range(len(equalSets)):
                if op1 in equalSets[idx]:
                    s1 = idx
                if op2 in equalSets[idx]:
                    s2 = idx
            if s1 is not None and s2 is not None:
                if s1 != s2:
                    equalSets[min(s1, s2)] = equalSets[s1].union(equalSets[s2])
                    del equalSets[max(s1, s2)]
            if s1 is None and s2 is not None:
                equalSets[s2].add(op1)
            if s1 is not None and s2 is None:
                equalSets[s1].add(op2)
            if s1 is None and s2 is None:
                equalSets.append({op1, op2})
    isTrue = True
    for i in inLi:
        if i[1] == "!":
            op1 = i[0]
            op2 = i[3]
            for j in equalSets:
                if op1 in j and op2 in j:
                    isTrue = False
                    break
            if not isTrue: break
    print(str(isTrue).lower())