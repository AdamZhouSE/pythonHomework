s = input()
s += '...'
b = 0
g = 0
i = 0
while i < len(s):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'y':
        b += 1
        i += 3
    elif s[i] == 'b' and s[i + 1] == 'o':
        b += 1
        i += 2
    elif s[i] == 'b':
        b += 1
        i += 1
    elif s[i] == 'o' and s[i + 1] == 'y':
        b += 1
        i += 2
    elif s[i] == 'o':
        b += 1
        i += 1
    elif s[i] == 'y':
        b += 1
        i += 1
    elif s[i] == 'g' and s[i + 1] == 'i' and s[i + 2] == 'r' and s[i + 3] == 'l':
        g += 1
        i += 4
    elif s[i] == 'g' and s[i + 1] == 'i' and s[i + 2] == 'r':
        g += 1
        i += 3
    elif s[i] == 'g' and s[i + 1] == 'i':
        g += 1
        i += 2
    elif s[i] == 'g':
        g += 1
        i += 1
    elif s[i] == 'i' and s[i + 1] == 'r' and s[i + 2] == 'l':
        g += 1
        i += 3
    elif s[i] == 'i' and s[i + 1] == 'r':
        g += 1
        i += 2
    elif s[i] == 'i':
        g += 1
        i += 1
    elif s[i] == 'r' and s[i + 1] == 'l':
        g += 1
        i += 2
    elif s[i] == 'r':
        g += 1
        i += 1
    elif s[i] == 'l':
        g += 1
        i += 1
    else:
        i += 1
print(b)
print(g,end='')