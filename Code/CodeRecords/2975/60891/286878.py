s = input()
s_list = []
for i in range(len(s)):
    s_list.append(s[i])
s_list.sort()
for i in range(len(s)):
    print(s_list[i], end='')

    