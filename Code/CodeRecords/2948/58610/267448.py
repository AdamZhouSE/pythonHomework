s = list(input())
key = eval(input())
res = ""
for ch in s:
    res += str(ord(ch) - ord('A') + key)
while int(res) > 100:
    temp = []
    for i in range(len(res) - 1):
        t = res[i:i + 2]
        temp.append(str((int(t[0]) + int(t[1])) % 10))
    res = ''.join(temp)
print(int(res), end='')