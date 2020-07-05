s, t = input().strip(), input().strip()
index = 0
for i in t:
    if s[index] == i:
        index += 1
    if index == len(s) - 1:
        print(True)
        break
else:
        print(False)