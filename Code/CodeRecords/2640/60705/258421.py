def contains(a, b):
    for i in range(0, len(b)):
        if b[i] not in a:
            return False
    return True


s = input()
t = input()
sub = []
for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        if contains(s[i:j], t):
            sub.append(s[i:j])
if len(sub) == 0:
    print("")
else:
    m = len(sub[0])
    index = 0
    for i in range(0, len(sub)):
        if len(sub[i]) < m:
            m = len(sub[i])
            index = i
    print(sub[index])
