s = input()
result = 0
for i in range(len(s)):
    result += (ord(s[i]) - 64) * pow(26, len(s) - 1 - i)
print(str(result))