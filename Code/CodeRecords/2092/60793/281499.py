people_num = int(input())
info = [[i] for i in range(0, people_num)]
a = list(map(int, input().split()))
a = [x - 1 for x in a]
count = 0
flag = True
while flag:
    count += 1
    temp_info = info[:]
    for i in range(0, len(info)):
        tar = info[a[i]]
        sou = info[i]
        if a[i] in sou:
            flag = False
        temp_info[a[i]] = list(set(tar) | set(sou))
    info = temp_info[:]
print(count)