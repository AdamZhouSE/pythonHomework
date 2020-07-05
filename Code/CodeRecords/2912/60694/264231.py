string = input()
max_len = 0
tmp = ""
for ch in string:
    if ch not in tmp:
        tmp += ch
    else:
        if len(tmp) > max_len:
            max_len = len(tmp)
        tmp = ch
print(max_len)
