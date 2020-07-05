# 12
s = input()
k = int(input())

def f(s,c):
    t = 0
    l = []
    for i in range(len(s)):
        if s[i] == c:
            t += 1
            l.append(t)
        else:
            t = 0
    return max(l)
no_r = set(list(s))
l = []
for c in no_r:
    m = []
    for i in range(len(s)):
        t = 0
        sub = s[:]
        for j in range(i,len(s)):
            if sub[j] != c:
                if t >= k:
                    break
                sub = sub[:j] + c + sub[j+1:]
                t += 1
        m.append(f(sub,c))
    l.append(max(m))
print(max(l))