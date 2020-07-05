a = input()
b = input()
ans = 0
for i in range(len(a) - len(b) + 1):
    if a[i:i + len(b)] == b:
        ans += 1
print(ans, end='')