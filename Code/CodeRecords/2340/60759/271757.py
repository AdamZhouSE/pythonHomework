t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    lst.insert(0, 0)
    lst.append(0)
    blocks = []
    greaters = []
    idx = 1
    while idx < len(lst) - 1:
        blocks.append([lst[idx], 1])
        offset = 1
        while idx + offset < len(lst) and lst[idx + offset] == lst[idx]:
            blocks[-1][1] += 1
            offset += 1
        if lst[idx - 1] < lst[idx] > lst[idx + offset]:
            greaters.append(len(blocks) - 1)
        idx += offset
    ans = 0
    for j in range(len(greaters) - 1):
        bound = min(blocks[greaters[j]][0], blocks[greaters[j + 1]][0])
        for k in range(greaters[j] + 1, greaters[j + 1]):
            ans += max(0, (bound - blocks[k][0]) * blocks[k][1])
    print(ans)
