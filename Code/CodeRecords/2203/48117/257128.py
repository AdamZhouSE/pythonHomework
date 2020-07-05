def findProffix(s: str, proffix: list) -> list:
    for i in range(len(s)):
        proffix.append(s[i:])
    return proffix

s = input()

for i in range(len(s)):
    proffix1 = []
    proffix1 = findProffix(s[:i + 1], proffix1)
    count = 0
    for j in range(i, len(s)):
        proffix2 = []
        if j == i:
            continue
        else:
            proffix2 = findProffix(s[:j + 1], proffix2)
            for proffix in proffix1:
                if proffix in proffix2:
                    count += len(proffix) - 1
    
    print(count % (pow(10, 9) + 7))