s = input()
s_list = []
for i in range(len(s)):
    if s[i] == '1':
        s_list.append(1)
    else:
        s_list.append(0)
count = 0
for i in range(len(s) - 1, -1, -1):
    # 0_i 首尾都取，翻转
    if s_list[i] == 0:
        for j in range(0, i + 1):
            s_list[j] = 1 - s_list[j]
        count += 1
print(count)