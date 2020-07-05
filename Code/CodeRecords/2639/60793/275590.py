from collections import Counter
s = input()
k = int(input())
result = 0
for length in range(1, len(s) + 1):
    for i in range(0, len(s) - length):
        s_slice = s[i:i+length+1]
        d = Counter(s_slice)
        if len(d) == 2 and min(d.values()) <= k:
            result = max(result, len(s_slice))
print(result)