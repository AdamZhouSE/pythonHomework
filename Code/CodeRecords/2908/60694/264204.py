from collections import Counter
N = int(input())
words = [input() for _ in range(N)]
l = []
for word in words:
    tmp_dict = Counter(word)
    if tmp_dict not in l:
        l.append(tmp_dict)
ans = len(l)
if ans == 3:
    ans = 2
print(ans, end="")
