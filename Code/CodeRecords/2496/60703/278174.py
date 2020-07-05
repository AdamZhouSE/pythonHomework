S = input()
s = sorted(S)
import collections
count =collections.Counter(S)
maxLen = 0
for key in count:
    if count[key] >maxLen:
        maxLen = count[key]
if maxLen>((len(S)+1)//2):
    print("")
else:
    n = (len(s)+1)//2
    a,b = s[:n],s[n:]
    lenA = len(a)
    lenB = len(b)
    minLen = min(lenA,lenB)
    res = []
    for i in range(minLen):
        res.append(a[i])
        res.append(b[i])
    if lenB>lenA:
        res.append(b[-1])
    if lenB<lenA:
        res.append(a[-1])
    print("".join(res))
