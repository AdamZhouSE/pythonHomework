n = int(input())
strings = []
for i in range(0, n):
    strings.append(input())
max_length = 0

for i in range(0, len(strings[0])):  # i：子串start index
    for j in range(i+1, len(strings[0])+1):  # j：子串end index

        s = strings[0][i:j]  # 切出子串
        all_contain = True  # 假设后面的所有字符串都含有这个字串
        for k in range(1, len(strings)):
            if not strings[k].__contains__(s):
                all_contain = False

        if all_contain and j - i > max_length:
            max_length = j - i

print(max_length)