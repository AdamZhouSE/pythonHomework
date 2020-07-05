s = input()
res = 0
for x in s:
    res *= 26
    res += ord(x) - ord('A') + 1
print(res)
