def proffix(s : str) -> list:
    ans = []
    for i in range(1, len(s) + 1):
        ans.append(s[:i])
    return ans



n = int(input())
s = input()
w_ = input().split(' ')
w = []
sw = dict()


for i in w_:
    w.append(int(i))


for i in range(len(s)):
    sw[s[i:]] = w[i]

suffix = list(sw.keys())
maxlen = 0
maxAns = 0
lcpW = 0
for i in range(len(suffix) - 1):
    for j in range(i + 1, len(suffix)):
        proffixi = proffix(suffix[i])
        proffixj = proffix(suffix[j])
        for p in proffixi:
            if p in proffixj:
                if len(p) > maxlen:
                    maxLen = len(p)

        lcpW = maxlen + (w[i] ^ w[j])
        if lcpW > maxAns:
            maxAns = lcpW

print(maxAns)