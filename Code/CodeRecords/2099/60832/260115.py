import math

excel = input()
length = len(excel)
ans = 0
for i in range(length):
    ans += int(math.pow(26, i)) * (ord(excel[length - i - 1]) - ord('A') + 1)
print(ans)
