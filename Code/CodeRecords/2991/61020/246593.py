s = input()

b = ''

i = len(s) - 1
while i >= 0:
    b += s[i]

    i -= 1

print(b, end='')
