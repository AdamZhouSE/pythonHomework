inp = input()
res = 0
for s in inp:
    res = res * 26 + ord(s) - ord('A') + 1
print(res)
