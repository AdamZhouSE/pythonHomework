people_num = int(input())
info = [[i] for i in range(0, people_num)]
a = list(map(int, input()))
a = [x - 1 for x in a]
count = 0
while True:
    count += 1
    for i in range(0, len(info)):
        tar = info[a[i]]
        sou = info[i]
        info[a[i]] = list(set(tar) | set(sou))
    for i in info:
        if i != [x for x in range(0, people_num)]:
            continue
    break
print(count)