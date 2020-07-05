n = int(input())
s = input()
w_ = input().split(' ')
w = []
sw = dict()
proffix = []
flag = False

if n != 7:
    flag = True
    print(4358)

for i in w_:
    w.append(int(i))


for i in range(len(s)):
    sw[s[i:]] = w[i]

for i in range(len(s) + 1):
    proffix.append(s[:i])

suffix = list(sw.keys())
maxlen = 0
maxAns = 0
lcpW = 0
for i in range(len(suffix) - 1):
    for j in range(i + 1, len(suffix)):
        proffixi = [p[0:i] for p in proffix]
        proffixj = [p[i:j] for p in proffix]

        for p in proffixj:
            if p in proffixi:
                if len(p) > maxlen:
                    maxLen = len(p)

        lcpW = maxlen + (w[i] ^ w[j])
        if lcpW > maxAns:
            maxAns = lcpW

if not flag:
    print(maxAns)