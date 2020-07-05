from collections import defaultdict


string = input()
ans = []
repeat = defaultdict(int)
for ch in string:
    counts = string.count(ch)
    if ch not in repeat:
        repeat[ch] = string.count(ch)
sort_r = list(map(list, sorted(repeat.items(), key=lambda x: x[1], reverse=True)))
ans.extend(sort_r[0][0] * sort_r[0][1])
idx = 1
pre = sort_r[0][1]
success = False
for i in range(1, len(sort_r)):
    if sort_r[i][1] == pre:
        ans.append(sort_r[i][0])
        sort_r[i][1] -= 1
        success = True
    for j in range(sort_r[i][1]):
        ans.insert(idx, sort_r[i][0])
        idx += 2
        if idx >= len(ans):
            success = True
            idx = 1
print(''.join(ans) if success else "")
