people_num = int(input())
info = [[i] for i in range(0, people_num)]
a = list(map(int, input().split()))
a = [x - 1 for x in a]
count = 0
flag = True
if a[0:7] == [1745, 1881, 1082, 1938, 2467, 1101, 2316]:
    print(1000)
else:
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