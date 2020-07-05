def find_same(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    madlen = 0
    p = 0
    for a in range(len(s1)):
        for b in range(len(s2)):
            if s1[a] == s2[b]:
                m[a + 1][b + 1] = m[a][b] + 1
                if m[a + 1][b + 1] > madlen:
                    madlen = m[a + 1][b + 1]
                    p = a + 1
    return madlen
#s1[p - madlen:p],

n = int(input())
text = []
for i in range(n):
    s = str(input())
    text.append(s)
res = []
for i in range(0, len(text) - 1):
    for j in range(i+1,len(text)):
        res.append(find_same(text[i], text[j]))
print(min(res))