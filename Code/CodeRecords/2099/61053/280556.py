str = input()
res = 0
for ch in str:
    res *= 26
    res += ord(ch) - ord('A') + 1
print(res)