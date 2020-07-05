from collections import Counter
N = int(input())
words = [input() for _ in range(N)]
l = []
cnt = 0
for word in words:
    tmp_dict = Counter(word)
    if tmp_dict not in l:
        l.append(tmp_dict)
        cnt += 1
print(cnt)
