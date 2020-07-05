s = input()
ans = 0
for c in s:
    ans = ans * 26 + ord(c) - 64
print(ans)