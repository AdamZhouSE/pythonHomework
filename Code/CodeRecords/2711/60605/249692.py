# 题目描述
# 如果我们交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。
# 如果这两个字符串本身是相等的，那它们也是相似的。
#
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)；
# "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
#
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。
# 注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
# 形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
#
# 我们给出了一个不包含重复的字符串列表 A。
# 列表中的每个字符串都是 A 中其它所有字符串的一个字母异位词。
# 请问 A 中有多少个相似字符串组？
#
# 注：字母异位词[anagram]，一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。

def union(li, set1, set2):
    if set1 == set2: return
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

def isSimilar(str1, str2) -> bool:
    cnt = 0
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            cnt += 1
            if cnt > 2: return False
    return True

if __name__ == '__main__':
    li = list(eval(input()))
    sets = [-1 for i in range(len(li))]

    for i in range(1, len(li)):
        for j in range(0, i):
            if isSimilar(li[i], li[j]):
                union(sets, find(sets, i), find(sets, j))
                break
    cnt = 0
    for i in sets:
        if i < 0: cnt += 1
    print(cnt)