s = input()
cnt = 0
for i in range(len(s)):
    if s[i] != ' ' or s[i] != '\n':
        cnt = cnt + 1
print(cnt, end = "")