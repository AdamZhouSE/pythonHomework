def pick(pos):
    pos = sorted(pos, key=len, reverse=True)
    l = len(pos[0])
    for s in pos:
        if len(s) < l:
            pos = pos[:pos.index(s)]
    for i in range(len(pos)):
        pos[i] = pos[i][::-1]
    return sorted(pos, reverse=True)[0]

def filter(line):
    i = 0
    pos = []
    while i < len(line):
        if i == len(line)-1:
            pos.append(line[-1])
            break
        start = i
        i += 1
        gap = ord(line[i]) - ord(line[i-1])
        i += 1
        while i < len(line):
            if ord(line[i]) - ord(line[i-1]) == gap:
                i += 1
            else:
                break
        pos.append(line[start:i])
    return pick(pos)    

def test():
    line = input()
    A.append(filter(line))

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)