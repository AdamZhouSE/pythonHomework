# 12
s = input()
k = int(input())

def f(s,c):
    t = 0
    for i in range(len(s)):
        if s[i] == c:
            t += 1
        else:
            t = 0
    return t
no_r = set(list(s))
l = []
for c in no_r:
    t = 0
    m = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] != c:
                if t >= k:
                    break
                s = s[:j] + c + s[j+1:]
                t += 1
        m.append(f(s,c))
    l.append(max(m))
print(max(l))