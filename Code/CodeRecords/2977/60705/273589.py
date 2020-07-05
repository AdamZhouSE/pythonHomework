strings = []
for line in iter(input, '!'):
    strings.append(list(line.strip()))

for x in strings:
    for i in range(0, len(x)):
        if 'a' <= x[i] <= 'z':
            x[i] = chr(219-ord(x[i]))
        elif 'A' <= x[i] <= 'Z':
            x[i] = chr(155-ord(x[i]))
        else:
            x[i] = x[i]
    b = ""
    for i in range(0, len(x)):
        b += x[i]
    print(b)