s = input()
maxlen = []
i = 0
while i < len(s):
    ss = ""
    j = i
    while j < len(s):
        if ss.find(s[j]) < 0:
            ss += s[j]
        else:
            break
        j += 1
    maxlen.append(len(ss))
    i += 1
maxlen = sorted(maxlen)
print(maxlen[len(maxlen)-1])