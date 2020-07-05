s = sorted(input().split("+"))
num = len(s)
print(s[0], end="")
for i in range(1, num):
    print("+"+s[i], end="")
print()