s=input()

def isValid(s: str) -> bool:
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        elif c == ")":
            cnt -= 1
        if cnt < 0: return False
    return cnt == 0



level = {s}
while True:
    valid = list(filter(isValid, level))
    if valid:
        print(valid)
        break
    next_level = set()
    for item in level:
        for i in range(len(item)):
            if item[i] in "()":
                next_level.add(item[:i] + item[i + 1:])
    level = next_level