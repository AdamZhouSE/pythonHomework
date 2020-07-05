from collections import Counter
N = int(input())
words = [input().strip() for _ in range(N)]
l = []
for word in words:
    tmp_dict = Counter(word)
    if tmp_dict not in l:
        l.append(tmp_dict)
ans = len(l)
print(ans, end="")
