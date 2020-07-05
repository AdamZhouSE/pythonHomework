s = input()
count = 0
for ch in s:
    if ch == ' ' or ch == '\n':
        continue
    else:
        count += 1
print(count, end='')
