from collections import defaultdict


lst = eval(input())
now = (0, 0)
roads = [lst[0][0]]
choices = defaultdict(int)
records = set()
records.add(now)
end = (len(lst) - 1, len(lst[0]) - 1)
while now != end:
    next_pos = [(now[0] + 1, now[1]), (now[0] - 1, now[1]), (now[0], now[1] + 1), (now[0], now[1] - 1)]
    if end in next_pos:
        roads.append(lst[end[0]][end[1]])
        break
    for pos in next_pos:
        if 0 <= pos[0] <= end[0] and 0 <= pos[1] <= end[1] and pos not in records:
            choices[pos] = lst[pos[0]][pos[1]]
    choices_s = sorted(choices.items(), key=lambda item: item[1])
    now = choices_s[0][0]
    records.add(now)
    roads.append(choices_s[0][1])
    choices.pop(now)
print(max(roads))
