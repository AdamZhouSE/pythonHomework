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
times = 0
for i in range(t):
    w = input()
    if i == 0:
        words.append(w)
        times += 1
    else:
        canFind = False
        for c in words:
            if check_word(w, c):
                canFind = True
                break
        if not canFind:
            words.append(w)
            times += 1
print(times)
