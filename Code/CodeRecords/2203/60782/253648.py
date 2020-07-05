"""
题目描述
    LJJ拿到了一串来自火星的字符串。
    字符串中，每个字符都是一种火星字母, LJJ 将其转换为小写英文字母a ~ z,为了便于发现其中的奥秘。
    仔细看，这个字符串杂乱中带着有序，有许多重复的片段。于是，LJJ请来了作为字符串分析专家的你，来帮他分析计算这个字符串的神秘度。
    设n是这个字符串的长度。设S[i, j]表示字符串S中第i个位置到第j个位置的连续子串(字符串下标从1开始)。
    若i,j, len同时满足:
        1 ≤ i < j ≤ i+len-1 < j+len-1 ≤ n
        S[i,i+len-1] = S[j,j+len-1]
    则这个三元数对(i, j, len)对S的神秘度的贡献是len。
    输入一个字符串，输出其所有前缀的神秘度。由于这个值过大,所以请对10^9 + 7取模并输出。
"""
"""
输入描述
    输入仅一行：仅由小写字母构成的字符串S。
"""
"""
输出描述
    输出共n行，第i行的整数是前i个位置表示的前缀的神秘度。
"""


def check_whether_mysterious(position_i, position_j, current_fix):
    contribution = 0
    for leng in range(position_j - position_i, len(current_fix)):
        if ((1 <= position_i < position_j <= position_i + leng - 1 < position_j + leng -1 <= len(current_fix))
                and (current_fix[position_i - 1:position_i + leng - 1] == current_fix[position_j - 1:position_j + leng - 1])):
            contribution = contribution + leng
            contribution = contribution % (10 ** 9 + 7)
    return contribution


def deal_with_each_prefix(str):
    mysterious_level = 0
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            mysterious_level = mysterious_level + check_whether_mysterious(i, j, str)
            mysterious_level = mysterious_level % (10 ** 9 + 7)
    return mysterious_level


string = input()
str = []
for end in range(1, len(string) + 1):
    str.append(string[:end])
for each_prefix in str:
    answer_of_each = deal_with_each_prefix(each_prefix)
    print(answer_of_each)


