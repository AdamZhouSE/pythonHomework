n = int(input())
strings = []
for i in range(0, n):
    strings.append(input())
max_length = 0

for i in range(0, len(strings[0])):  # i：字串start index
    for j in range(i+1, len(strings[0])):  # j：字串end index

        s = strings[0][i:j]  # 切出字串
        all_contain = True
        for k in range(1, len(strings)):
            if not strings[k].__contains__(s):
                all_contain = False

        if all_contain and j - i > max_length:
            max_length = j - i

print(max_length)