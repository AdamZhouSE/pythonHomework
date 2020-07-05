
s=input()
k=int(input())
lookup = {}
start, end, max_freq, res = 0, 0, 0, 0
while end < len(s):
    lookup[s[end]] = lookup.get(s[end], 0) + 1
    max_freq = max(max_freq, lookup[s[end]])
    if end - start + 1 - max_freq > k: # 这里为什么用if不用while呢？见下方解析
        lookup[s[start]] -= 1
        start += 1
    end += 1
    res = max(res, end - start)
print(res)