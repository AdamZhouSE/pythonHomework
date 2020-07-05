"""
串联字符串的最大长度
要得到一个字符串，每个字母都不相同
"""


def not_repeat(s):
    lent = len(s)
    s1 = set(s)
    if len(s1) < lent:
        return False
    else:
        return True


inp = eval(input())
data = []
max_len = 0
curr_len = 0
for i in range(len(inp)):
    sequence = inp[i]
    if not_repeat(sequence):
        data.append(sequence)
        curr_len = len(sequence)
    for j in range(i+1, len(inp)):
        sequence += inp[j]
        if not_repeat(sequence):
            data.append(sequence)
            curr_len = len(sequence)
    if max_len < curr_len:
        max_len = curr_len
print(max_len)
