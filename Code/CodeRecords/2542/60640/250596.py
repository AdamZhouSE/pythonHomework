import re
inp = re.split(r"[\[\],]", input())
data = []
for c in inp:
    if c != "":
        data.append(int(c))
data.sort()
max_len = 1
curr_len = 1
for i in range(0, len(data)-1):
    # 如果是连续，则当前子序列长度加1
    if data[i+1]-data[i] == 1:
        curr_len += 1
    # 如果不连续，则判断当前子序列长度是否大于最大子序列长度，
    else:
        if curr_len > max_len:
            max_len = curr_len
        # 不连续代表当前子序列结束，重置长度
        curr_len = 1
print(max_len)
