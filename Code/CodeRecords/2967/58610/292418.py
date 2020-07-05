s = [input() for _ in range(eval(input()))]

def find_lcs(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    max_s = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > max_s:
                    max_s = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - max_s:p]

a = s[0]
for string in s:
    a = find_lcs(a, string)
print(len(a))