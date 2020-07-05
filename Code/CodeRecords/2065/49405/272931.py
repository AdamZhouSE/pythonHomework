s = list(input())
for c in s:
    if c != "-" or not c.isdigit():
        s.remove(c)
print(max(min(int("".join(s)), 2147483647), -2147483648))