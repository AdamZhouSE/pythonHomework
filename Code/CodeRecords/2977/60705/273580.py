strings = []
for line in iter(input, '!'):
    strings.append(list(line.strip()))

for x in strings:
    for i in range(0, len(x)):
        if 'a' <= x[i] <= 'z':
            x[i] = chr(ord('z') - ord(x[i]) + ord('a'))
        elif 'A' <= x[i] <= 'Z':
            x[i] = chr(ord('Z') - ord(x[i]) + ord('A'))
    for i in x:
        print(i, end="")
    print()