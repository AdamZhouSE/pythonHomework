import copy

s = input()
# b = copy.copy(s)
b = s

i = len(s) - 1
while i >= 0:
    b += s[i]

    i -= 1

print(b)
