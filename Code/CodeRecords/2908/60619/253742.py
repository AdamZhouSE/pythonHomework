def check_word(s, target):
    result = True
    if len(s) != len(target):
        result = False
    for ind in s:
        if s.count(ind) != target.count(ind):
            result = False
            break
    return result


t = int(input())
words = []
for i in range(t):
    w = input()
    if i == 0:
        words.append(w)
    else:
        canFind = False
        for c in words:
            if check_word(w, c):
                canFind = True
                break
        if not canFind:
            words.append(w)
print(len(words)-1)
