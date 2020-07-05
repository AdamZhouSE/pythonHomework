s = input()
s = s[1:len(s) - 1].split(", ")
arr = dict.fromkeys(s, 0)
maxlen = 0
for i in s:
    left = arr.get(str(int(i) - 1), 0)
    right = arr.get(str(int(i) + 1), 0)
    arr[i] = left + right + 1
    if left != 0:
        arr[str(int(i) - left)] = left + right + 1
    if right != 0:
        arr[str(int(i) + right)] = left + right + 1
    maxlen = max(maxlen, left + right + 1)
print(maxlen)