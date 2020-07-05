from collections import Counter

s = input()
t = input()

t = Counter(t)
lookup = Counter()
start = 0
end = 0
min_len = float("inf")
res = ""

while end < len(s):
    lookup[s[end]] += 1
    end += 1
    while all(map(lambda x: lookup[x] >= t[x], t.keys())):
        if end - start < min_len:
            res = s[start:end]
            min_len = end - start
        lookup[s[start]] -= 1
        start += 1

print(res)
